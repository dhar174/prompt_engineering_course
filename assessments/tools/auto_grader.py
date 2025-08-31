#!/usr/bin/env python3
"""
Automated Grading Tools for Prompt Engineering Course

This module provides automated grading capabilities for various assessment types
including quizzes, code labs, and structured assignments.
"""

import json
import re
import ast
import subprocess
import tempfile
import os
from typing import Dict, List, Optional, Any, Tuple, Union
from dataclasses import dataclass, asdict
from abc import ABC, abstractmethod
from datetime import datetime
import tiktoken
import openai
from textstat import flesch_reading_ease, flesch_kincaid_grade
import pandas as pd


@dataclass
class GradingResult:
    """Result of automated grading"""
    score: float
    max_score: float
    percentage: float
    feedback: str
    details: Dict[str, Any]
    execution_time: float
    graded_at: datetime
    
    def __post_init__(self):
        self.percentage = (self.score / self.max_score) * 100 if self.max_score > 0 else 0


@dataclass
class TestCase:
    """Individual test case for code evaluation"""
    name: str
    input_data: Any
    expected_output: Any
    timeout: int = 30
    points: float = 1.0
    description: str = ""
    
    
@dataclass
class RubricCriterion:
    """Rubric criterion for evaluation"""
    name: str
    description: str
    max_points: float
    weight: float = 1.0
    auto_gradable: bool = True
    evaluation_method: str = "exact_match"  # exact_match, similarity, llm_judge


class AutoGrader(ABC):
    """Abstract base class for automated graders"""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.start_time = None
        
    @abstractmethod
    def grade(self, submission: Any) -> GradingResult:
        """Grade a submission and return results"""
        pass
    
    def _start_timer(self):
        """Start timing the grading process"""
        self.start_time = datetime.now()
    
    def _get_execution_time(self) -> float:
        """Get execution time in seconds"""
        if self.start_time:
            return (datetime.now() - self.start_time).total_seconds()
        return 0.0


class QuizGrader(AutoGrader):
    """Automated grader for quiz assessments"""
    
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.questions = config.get('questions', [])
        self.partial_credit = config.get('partial_credit', True)
        self.case_sensitive = config.get('case_sensitive', False)
        
    def grade(self, submission: Dict[str, Any]) -> GradingResult:
        """Grade quiz submission"""
        self._start_timer()
        
        total_score = 0
        max_score = 0
        feedback_parts = []
        details = {}
        
        student_answers = submission.get('answers', {})
        
        for question in self.questions:
            question_id = question['id']
            question_type = question['type']
            question_points = question.get('points', 1)
            
            max_score += question_points
            
            if question_id not in student_answers:
                feedback_parts.append(f"Question {question_id}: No answer provided")
                details[question_id] = {
                    'score': 0,
                    'max_score': question_points,
                    'feedback': "No answer provided"
                }
                continue
            
            student_answer = student_answers[question_id]
            
            # Grade based on question type
            if question_type == 'multiple_choice_single':
                score, feedback = self._grade_multiple_choice_single(question, student_answer)
            elif question_type == 'multiple_choice_multiple':
                score, feedback = self._grade_multiple_choice_multiple(question, student_answer)
            elif question_type == 'true_false':
                score, feedback = self._grade_true_false(question, student_answer)
            elif question_type == 'short_answer':
                score, feedback = self._grade_short_answer(question, student_answer)
            elif question_type == 'matching':
                score, feedback = self._grade_matching(question, student_answer)
            elif question_type == 'ordering':
                score, feedback = self._grade_ordering(question, student_answer)
            else:
                score, feedback = 0, f"Unknown question type: {question_type}"
            
            question_score = score * question_points
            total_score += question_score
            
            feedback_parts.append(f"Question {question_id}: {feedback}")
            details[question_id] = {
                'score': question_score,
                'max_score': question_points,
                'feedback': feedback,
                'type': question_type
            }
        
        overall_feedback = "\n".join(feedback_parts)
        
        return GradingResult(
            score=total_score,
            max_score=max_score,
            percentage=(total_score / max_score) * 100 if max_score > 0 else 0,
            feedback=overall_feedback,
            details=details,
            execution_time=self._get_execution_time(),
            graded_at=datetime.now()
        )
    
    def _grade_multiple_choice_single(self, question: Dict, student_answer: str) -> Tuple[float, str]:
        """Grade single-answer multiple choice question"""
        correct_answer = question.get('correct_answer', '')
        
        if not self.case_sensitive:
            student_answer = student_answer.lower()
            correct_answer = correct_answer.lower()
        
        if student_answer == correct_answer:
            return 1.0, "Correct! " + question.get('explanation', '')
        else:
            return 0.0, "Incorrect. " + question.get('explanation', '')
    
    def _grade_multiple_choice_multiple(self, question: Dict, student_answer: List[str]) -> Tuple[float, str]:
        """Grade multiple-answer multiple choice question"""
        correct_answers = set(question.get('correct_answers', []))
        student_set = set(student_answer) if isinstance(student_answer, list) else {student_answer}
        
        if not self.case_sensitive:
            correct_answers = {ans.lower() for ans in correct_answers}
            student_set = {ans.lower() for ans in student_set}
        
        if student_set == correct_answers:
            return 1.0, "Correct! " + question.get('explanation', '')
        elif self.partial_credit:
            # Calculate partial credit
            correct_selected = len(student_set & correct_answers)
            incorrect_selected = len(student_set - correct_answers)
            missed_correct = len(correct_answers - student_set)
            
            # Partial credit formula: (correct - incorrect) / total_correct
            partial_score = max(0, (correct_selected - incorrect_selected) / len(correct_answers))
            
            feedback = f"Partially correct. Selected {correct_selected}/{len(correct_answers)} correct answers"
            if incorrect_selected > 0:
                feedback += f" and {incorrect_selected} incorrect answers"
            feedback += ". " + question.get('explanation', '')
            
            return partial_score, feedback
        else:
            return 0.0, "Incorrect. " + question.get('explanation', '')
    
    def _grade_true_false(self, question: Dict, student_answer: Union[bool, str]) -> Tuple[float, str]:
        """Grade true/false question"""
        correct_answer = question.get('correct_answer', False)
        
        # Convert string answers to boolean
        if isinstance(student_answer, str):
            student_answer = student_answer.lower() in ['true', 't', '1', 'yes', 'y']
        
        if student_answer == correct_answer:
            return 1.0, "Correct! " + question.get('explanation', '')
        else:
            return 0.0, "Incorrect. " + question.get('explanation', '')
    
    def _grade_short_answer(self, question: Dict, student_answer: str) -> Tuple[float, str]:
        """Grade short answer question"""
        keywords = question.get('keywords', [])
        sample_answers = question.get('sample_answers', [])
        
        if not keywords and not sample_answers:
            # Cannot auto-grade without keywords or sample answers
            return 0.0, "Manual grading required"
        
        student_answer_lower = student_answer.lower() if not self.case_sensitive else student_answer
        
        # Check for keywords
        keyword_score = 0
        if keywords:
            found_keywords = sum(1 for keyword in keywords if keyword.lower() in student_answer_lower)
            keyword_score = found_keywords / len(keywords)
        
        # Check similarity to sample answers
        similarity_score = 0
        if sample_answers:
            similarities = []
            for sample in sample_answers:
                sample_lower = sample.lower() if not self.case_sensitive else sample
                # Simple similarity based on common words
                student_words = set(student_answer_lower.split())
                sample_words = set(sample_lower.split())
                if sample_words:
                    similarity = len(student_words & sample_words) / len(sample_words)
                    similarities.append(similarity)
            
            if similarities:
                similarity_score = max(similarities)
        
        # Combine scores
        final_score = max(keyword_score, similarity_score) if keywords and sample_answers else (keyword_score or similarity_score)
        
        if final_score >= 0.8:
            return 1.0, "Excellent answer!"
        elif final_score >= 0.6:
            return 0.8, "Good answer, but could be more complete"
        elif final_score >= 0.4:
            return 0.6, "Partial answer, missing some key concepts"
        else:
            return 0.0, "Answer does not address the question adequately"
    
    def _grade_matching(self, question: Dict, student_answer: Dict[str, str]) -> Tuple[float, str]:
        """Grade matching question"""
        correct_matches = question.get('correct_matches', {})
        
        if not correct_matches:
            return 0.0, "No correct matches provided"
        
        correct_count = 0
        total_matches = len(correct_matches)
        
        for left_item, correct_right in correct_matches.items():
            if left_item in student_answer:
                student_right = student_answer[left_item]
                if not self.case_sensitive:
                    student_right = student_right.lower()
                    correct_right = correct_right.lower()
                
                if student_right == correct_right:
                    correct_count += 1
        
        score = correct_count / total_matches if total_matches > 0 else 0
        
        if score == 1.0:
            return 1.0, "All matches correct!"
        elif score >= 0.8:
            return score, f"Good! {correct_count}/{total_matches} matches correct"
        elif score >= 0.5:
            return score, f"Partial success: {correct_count}/{total_matches} matches correct"
        else:
            return score, f"Needs improvement: only {correct_count}/{total_matches} matches correct"
    
    def _grade_ordering(self, question: Dict, student_answer: List[str]) -> Tuple[float, str]:
        """Grade ordering/sequencing question"""
        correct_order = question.get('correct_order', [])
        
        if not correct_order:
            return 0.0, "No correct order provided"
        
        if len(student_answer) != len(correct_order):
            return 0.0, "Incorrect number of items in sequence"
        
        # Check for exact match
        if student_answer == correct_order:
            return 1.0, "Perfect sequence!"
        
        # Partial credit for adjacent swaps
        if self.partial_credit:
            score = self._calculate_sequence_similarity(student_answer, correct_order)
            if score >= 0.8:
                return score, "Nearly correct sequence with minor errors"
            elif score >= 0.6:
                return score, "Partially correct sequence"
            else:
                return score, "Sequence has significant errors"
        
        return 0.0, "Incorrect sequence"
    
    def _calculate_sequence_similarity(self, student_order: List[str], correct_order: List[str]) -> float:
        """Calculate similarity between two sequences"""
        if len(student_order) != len(correct_order):
            return 0.0
        
        # Count positions that are correct
        correct_positions = sum(1 for i, item in enumerate(student_order) if item == correct_order[i])
        
        # Bonus for adjacent items that are correctly ordered relative to each other
        relative_order_bonus = 0
        for i in range(len(correct_order) - 1):
            for j in range(i + 1, len(correct_order)):
                correct_i_pos = correct_order.index(correct_order[i])
                correct_j_pos = correct_order.index(correct_order[j])
                
                try:
                    student_i_pos = student_order.index(correct_order[i])
                    student_j_pos = student_order.index(correct_order[j])
                    
                    if (correct_i_pos < correct_j_pos and student_i_pos < student_j_pos) or \
                       (correct_i_pos > correct_j_pos and student_i_pos > student_j_pos):
                        relative_order_bonus += 1
                except ValueError:
                    # Item not found in student order
                    pass
        
        total_pairs = len(correct_order) * (len(correct_order) - 1) // 2
        relative_score = relative_order_bonus / total_pairs if total_pairs > 0 else 0
        
        # Combine exact position score and relative order score
        return (correct_positions / len(correct_order)) * 0.7 + relative_score * 0.3


class CodeLabGrader(AutoGrader):
    """Automated grader for code lab assessments"""
    
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.test_cases = [TestCase(**tc) for tc in config.get('test_cases', [])]
        self.rubric = [RubricCriterion(**rc) for rc in config.get('rubric', [])]
        self.language = config.get('language', 'python')
        self.allowed_imports = config.get('allowed_imports', [])
        self.forbidden_patterns = config.get('forbidden_patterns', [])
        
    def grade(self, submission: Dict[str, Any]) -> GradingResult:
        """Grade code lab submission"""
        self._start_timer()
        
        code = submission.get('code', '')
        if not code:
            return GradingResult(
                score=0,
                max_score=sum(tc.points for tc in self.test_cases),
                percentage=0,
                feedback="No code submitted",
                details={'error': 'No code provided'},
                execution_time=self._get_execution_time(),
                graded_at=datetime.now()
            )
        
        # Static analysis
        static_results = self._static_analysis(code)
        
        # Dynamic testing
        test_results = self._run_tests(code)
        
        # Rubric evaluation
        rubric_results = self._evaluate_rubric(code, test_results)
        
        # Combine results
        total_score = sum(result['score'] for result in test_results.values())
        max_score = sum(tc.points for tc in self.test_cases)
        
        feedback_parts = []
        
        # Add static analysis feedback
        if static_results['errors']:
            feedback_parts.append("Static Analysis Issues:")
            feedback_parts.extend(f"  - {error}" for error in static_results['errors'])
        
        # Add test results feedback
        feedback_parts.append("Test Results:")
        for test_name, result in test_results.items():
            status = "PASS" if result['passed'] else "FAIL"
            feedback_parts.append(f"  {test_name}: {status} ({result['score']}/{result['max_score']} points)")
            if result['feedback']:
                feedback_parts.append(f"    {result['feedback']}")
        
        # Add rubric feedback
        if rubric_results:
            feedback_parts.append("Code Quality:")
            for criterion, result in rubric_results.items():
                feedback_parts.append(f"  {criterion}: {result['score']}/{result['max_score']} points")
                if result['feedback']:
                    feedback_parts.append(f"    {result['feedback']}")
        
        overall_feedback = "\n".join(feedback_parts)
        
        details = {
            'static_analysis': static_results,
            'test_results': test_results,
            'rubric_results': rubric_results
        }
        
        return GradingResult(
            score=total_score,
            max_score=max_score,
            percentage=(total_score / max_score) * 100 if max_score > 0 else 0,
            feedback=overall_feedback,
            details=details,
            execution_time=self._get_execution_time(),
            graded_at=datetime.now()
        )
    
    def _static_analysis(self, code: str) -> Dict[str, Any]:
        """Perform static analysis on code"""
        results = {
            'errors': [],
            'warnings': [],
            'metrics': {}
        }
        
        try:
            # Parse the code
            tree = ast.parse(code)
            
            # Check for forbidden patterns
            for pattern in self.forbidden_patterns:
                if re.search(pattern, code):
                    results['errors'].append(f"Forbidden pattern detected: {pattern}")
            
            # Check imports
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        if alias.name not in self.allowed_imports:
                            results['warnings'].append(f"Unexpected import: {alias.name}")
                elif isinstance(node, ast.ImportFrom):
                    if node.module not in self.allowed_imports:
                        results['warnings'].append(f"Unexpected import: {node.module}")
            
            # Basic metrics
            results['metrics'] = {
                'lines_of_code': len([line for line in code.split('\n') if line.strip()]),
                'functions': len([node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]),
                'classes': len([node for node in ast.walk(tree) if isinstance(node, ast.ClassDef)])
            }
            
        except SyntaxError as e:
            results['errors'].append(f"Syntax error: {e}")
        except Exception as e:
            results['errors'].append(f"Analysis error: {e}")
        
        return results
    
    def _run_tests(self, code: str) -> Dict[str, Any]:
        """Run test cases against the code"""
        results = {}
        
        for test_case in self.test_cases:
            try:
                # Create a temporary file with the code
                with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
                    f.write(code)
                    temp_file = f.name
                
                # Run the test
                result = self._execute_test_case(temp_file, test_case)
                results[test_case.name] = result
                
            except Exception as e:
                results[test_case.name] = {
                    'passed': False,
                    'score': 0,
                    'max_score': test_case.points,
                    'feedback': f"Test execution error: {e}",
                    'output': '',
                    'expected': test_case.expected_output
                }
            finally:
                # Clean up temporary file
                try:
                    os.unlink(temp_file)
                except:
                    pass
        
        return results
    
    def _execute_test_case(self, code_file: str, test_case: TestCase) -> Dict[str, Any]:
        """Execute a single test case"""
        try:
            # Prepare the test script
            test_script = f"""
import sys
sys.path.insert(0, '{os.path.dirname(code_file)}')
import {os.path.basename(code_file)[:-3]}  # Import without .py extension

# Test case execution
input_data = {repr(test_case.input_data)}
expected_output = {repr(test_case.expected_output)}

# Execute the test
try:
    # This is a simplified test execution - would need to be more sophisticated
    # for different types of functions and test scenarios
    result = main(input_data) if 'main' in dir() else None
    print(f"RESULT: {{result}}")
except Exception as e:
    print(f"ERROR: {{e}}")
"""
            
            # Execute the test
            process = subprocess.run(
                ['python', '-c', test_script],
                capture_output=True,
                text=True,
                timeout=test_case.timeout
            )
            
            output = process.stdout.strip()
            error = process.stderr.strip()
            
            if process.returncode == 0 and not error:
                # Extract result from output
                if output.startswith("RESULT: "):
                    actual_output = output[8:]  # Remove "RESULT: " prefix
                    
                    # Compare with expected output
                    if str(actual_output) == str(test_case.expected_output):
                        return {
                            'passed': True,
                            'score': test_case.points,
                            'max_score': test_case.points,
                            'feedback': 'Test passed successfully',
                            'output': actual_output,
                            'expected': test_case.expected_output
                        }
                    else:
                        return {
                            'passed': False,
                            'score': 0,
                            'max_score': test_case.points,
                            'feedback': f'Expected {test_case.expected_output}, got {actual_output}',
                            'output': actual_output,
                            'expected': test_case.expected_output
                        }
                else:
                    return {
                        'passed': False,
                        'score': 0,
                        'max_score': test_case.points,
                        'feedback': 'No result produced',
                        'output': output,
                        'expected': test_case.expected_output
                    }
            else:
                return {
                    'passed': False,
                    'score': 0,
                    'max_score': test_case.points,
                    'feedback': f'Execution error: {error}',
                    'output': output,
                    'expected': test_case.expected_output
                }
                
        except subprocess.TimeoutExpired:
            return {
                'passed': False,
                'score': 0,
                'max_score': test_case.points,
                'feedback': f'Test timed out after {test_case.timeout} seconds',
                'output': '',
                'expected': test_case.expected_output
            }
        except Exception as e:
            return {
                'passed': False,
                'score': 0,
                'max_score': test_case.points,
                'feedback': f'Test execution error: {e}',
                'output': '',
                'expected': test_case.expected_output
            }
    
    def _evaluate_rubric(self, code: str, test_results: Dict[str, Any]) -> Dict[str, Any]:
        """Evaluate code against rubric criteria"""
        results = {}
        
        for criterion in self.rubric:
            if criterion.auto_gradable:
                score, feedback = self._evaluate_criterion(code, criterion, test_results)
                results[criterion.name] = {
                    'score': score,
                    'max_score': criterion.max_points,
                    'feedback': feedback
                }
        
        return results
    
    def _evaluate_criterion(self, code: str, criterion: RubricCriterion, test_results: Dict[str, Any]) -> Tuple[float, str]:
        """Evaluate a single rubric criterion"""
        # This is a simplified implementation - would need more sophisticated evaluation
        # based on the specific criterion type
        
        if criterion.name.lower() == 'code_quality':
            return self._evaluate_code_quality(code)
        elif criterion.name.lower() == 'functionality':
            return self._evaluate_functionality(test_results)
        elif criterion.name.lower() == 'efficiency':
            return self._evaluate_efficiency(code)
        else:
            return 0.0, "Manual evaluation required"
    
    def _evaluate_code_quality(self, code: str) -> Tuple[float, str]:
        """Evaluate code quality"""
        score = 0.0
        feedback_parts = []
        
        # Check for docstrings
        if '"""' in code or "'''" in code:
            score += 0.3
            feedback_parts.append("Good: Documentation present")
        else:
            feedback_parts.append("Missing: Function/class documentation")
        
        # Check for meaningful variable names
        if re.search(r'\b[a-zA-Z_][a-zA-Z0-9_]{2,}\b', code):
            score += 0.2
            feedback_parts.append("Good: Meaningful variable names")
        
        # Check for proper spacing
        if not re.search(r'[a-zA-Z0-9]\+[a-zA-Z0-9]', code):  # No spaces around operators
            score += 0.2
            feedback_parts.append("Good: Proper spacing")
        
        # Check for reasonable line length
        long_lines = [line for line in code.split('\n') if len(line) > 100]
        if not long_lines:
            score += 0.3
            feedback_parts.append("Good: Reasonable line length")
        else:
            feedback_parts.append(f"Issue: {len(long_lines)} lines exceed 100 characters")
        
        return score, "; ".join(feedback_parts)
    
    def _evaluate_functionality(self, test_results: Dict[str, Any]) -> Tuple[float, str]:
        """Evaluate functionality based on test results"""
        total_tests = len(test_results)
        passed_tests = sum(1 for result in test_results.values() if result['passed'])
        
        if total_tests == 0:
            return 0.0, "No tests available"
        
        score = passed_tests / total_tests
        return score, f"Passed {passed_tests}/{total_tests} tests"
    
    def _evaluate_efficiency(self, code: str) -> Tuple[float, str]:
        """Evaluate code efficiency"""
        # This is a very basic efficiency check
        # In practice, you'd want more sophisticated analysis
        
        score = 1.0
        feedback_parts = []
        
        # Check for nested loops (potential O(n²) complexity)
        nested_loop_count = len(re.findall(r'for.*:\s*\n\s*for', code))
        if nested_loop_count > 0:
            score -= 0.3
            feedback_parts.append(f"Concern: {nested_loop_count} nested loops detected")
        
        # Check for list comprehensions (generally more efficient)
        if '[' in code and 'for' in code and 'in' in code:
            score += 0.1
            feedback_parts.append("Good: List comprehensions used")
        
        return min(score, 1.0), "; ".join(feedback_parts) if feedback_parts else "Efficiency appears reasonable"


class PromptGrader(AutoGrader):
    """Automated grader for prompt engineering assessments"""
    
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.openai_client = openai.OpenAI() if config.get('use_openai') else None
        self.tokenizer = tiktoken.encoding_for_model("gpt-4")
        self.evaluation_criteria = config.get('evaluation_criteria', {})
        
    def grade(self, submission: Dict[str, Any]) -> GradingResult:
        """Grade prompt engineering submission"""
        self._start_timer()
        
        prompt = submission.get('prompt', '')
        expected_output = submission.get('expected_output', '')
        actual_output = submission.get('actual_output', '')
        
        if not prompt:
            return GradingResult(
                score=0,
                max_score=100,
                percentage=0,
                feedback="No prompt submitted",
                details={'error': 'No prompt provided'},
                execution_time=self._get_execution_time(),
                graded_at=datetime.now()
            )
        
        # Evaluate different aspects of the prompt
        results = {}
        
        # 1. Token efficiency
        results['token_efficiency'] = self._evaluate_token_efficiency(prompt)
        
        # 2. Clarity and structure
        results['clarity'] = self._evaluate_clarity(prompt)
        
        # 3. Output quality (if outputs provided)
        if actual_output and expected_output:
            results['output_quality'] = self._evaluate_output_quality(actual_output, expected_output)
        
        # 4. Prompt engineering techniques
        results['techniques'] = self._evaluate_techniques(prompt)
        
        # 5. Reading level appropriateness
        results['reading_level'] = self._evaluate_reading_level(prompt)
        
        # Calculate overall score
        total_score = 0
        max_score = 0
        feedback_parts = []
        
        for criterion, result in results.items():
            weight = self.evaluation_criteria.get(criterion, {}).get('weight', 1.0)
            max_points = self.evaluation_criteria.get(criterion, {}).get('max_points', 20)
            
            score = result['score'] * max_points
            total_score += score * weight
            max_score += max_points * weight
            
            feedback_parts.append(f"{criterion.title()}: {score:.1f}/{max_points} points - {result['feedback']}")
        
        overall_feedback = "\n".join(feedback_parts)
        
        return GradingResult(
            score=total_score,
            max_score=max_score,
            percentage=(total_score / max_score) * 100 if max_score > 0 else 0,
            feedback=overall_feedback,
            details=results,
            execution_time=self._get_execution_time(),
            graded_at=datetime.now()
        )
    
    def _evaluate_token_efficiency(self, prompt: str) -> Dict[str, Any]:
        """Evaluate token efficiency of the prompt"""
        tokens = self.tokenizer.encode(prompt)
        token_count = len(tokens)
        
        # Basic efficiency metrics
        words = prompt.split()
        word_count = len(words)
        chars_per_token = len(prompt) / token_count if token_count > 0 else 0
        
        # Scoring based on reasonable token usage
        if token_count <= 50:
            score = 1.0
            feedback = "Excellent: Concise and efficient token usage"
        elif token_count <= 100:
            score = 0.8
            feedback = "Good: Reasonable token usage"
        elif token_count <= 200:
            score = 0.6
            feedback = "Acceptable: Could be more concise"
        else:
            score = 0.4
            feedback = "Needs improvement: Very long prompt, consider reducing"
        
        return {
            'score': score,
            'feedback': feedback,
            'details': {
                'token_count': token_count,
                'word_count': word_count,
                'chars_per_token': chars_per_token
            }
        }
    
    def _evaluate_clarity(self, prompt: str) -> Dict[str, Any]:
        """Evaluate clarity and structure of the prompt"""
        score = 0.0
        feedback_parts = []
        
        # Check for clear instructions
        instruction_indicators = ['please', 'explain', 'describe', 'analyze', 'compare', 'list', 'provide']
        if any(indicator in prompt.lower() for indicator in instruction_indicators):
            score += 0.3
            feedback_parts.append("Good: Clear instruction words present")
        
        # Check for structure (bullet points, numbering, etc.)
        if re.search(r'[0-9]\.|•|\*|-', prompt):
            score += 0.2
            feedback_parts.append("Good: Structured format used")
        
        # Check for context setting
        context_indicators = ['context', 'background', 'situation', 'scenario']
        if any(indicator in prompt.lower() for indicator in context_indicators):
            score += 0.2
            feedback_parts.append("Good: Context provided")
        
        # Check for examples
        if 'example' in prompt.lower() or 'for instance' in prompt.lower():
            score += 0.2
            feedback_parts.append("Good: Examples provided")
        
        # Check for constraints
        constraint_indicators = ['must', 'should', 'limit', 'maximum', 'minimum', 'exactly']
        if any(indicator in prompt.lower() for indicator in constraint_indicators):
            score += 0.1
            feedback_parts.append("Good: Clear constraints specified")
        
        return {
            'score': score,
            'feedback': "; ".join(feedback_parts) if feedback_parts else "Could be clearer and more structured",
            'details': {
                'has_instructions': score >= 0.3,
                'has_structure': score >= 0.2,
                'has_context': 'context' in prompt.lower()
            }
        }
    
    def _evaluate_output_quality(self, actual_output: str, expected_output: str) -> Dict[str, Any]:
        """Evaluate quality of the output produced by the prompt"""
        if not actual_output or not expected_output:
            return {
                'score': 0.0,
                'feedback': "Cannot evaluate output quality without both actual and expected outputs",
                'details': {}
            }
        
        # Simple similarity check (in practice, would use more sophisticated methods)
        actual_words = set(actual_output.lower().split())
        expected_words = set(expected_output.lower().split())
        
        if expected_words:
            similarity = len(actual_words & expected_words) / len(expected_words)
        else:
            similarity = 0.0
        
        # Length comparison
        length_ratio = len(actual_output) / len(expected_output) if expected_output else 0
        length_score = 1.0 - abs(1.0 - length_ratio) if length_ratio <= 2.0 else 0.0
        
        # Combined score
        combined_score = (similarity * 0.7) + (length_score * 0.3)
        
        if combined_score >= 0.8:
            feedback = "Excellent: Output closely matches expectations"
        elif combined_score >= 0.6:
            feedback = "Good: Output is reasonably close to expectations"
        elif combined_score >= 0.4:
            feedback = "Acceptable: Output has some similarities but could be improved"
        else:
            feedback = "Needs improvement: Output differs significantly from expectations"
        
        return {
            'score': combined_score,
            'feedback': feedback,
            'details': {
                'similarity': similarity,
                'length_ratio': length_ratio,
                'length_score': length_score
            }
        }
    
    def _evaluate_techniques(self, prompt: str) -> Dict[str, Any]:
        """Evaluate use of prompt engineering techniques"""
        score = 0.0
        feedback_parts = []
        techniques_used = []
        
        # Check for common techniques
        techniques = {
            'few_shot': ['example', 'for instance', 'such as'],
            'chain_of_thought': ['step by step', 'think through', 'reasoning'],
            'role_playing': ['you are', 'act as', 'pretend'],
            'constraints': ['must', 'should not', 'exactly', 'limit'],
            'output_format': ['json', 'bullet points', 'numbered list', 'table']
        }
        
        for technique, indicators in techniques.items():
            if any(indicator in prompt.lower() for indicator in indicators):
                score += 0.2
                techniques_used.append(technique)
                feedback_parts.append(f"Good: {technique.replace('_', ' ').title()} technique used")
        
        # Bonus for multiple techniques
        if len(techniques_used) >= 3:
            score += 0.1
            feedback_parts.append("Excellent: Multiple techniques combined effectively")
        
        return {
            'score': min(score, 1.0),
            'feedback': "; ".join(feedback_parts) if feedback_parts else "Consider using more prompt engineering techniques",
            'details': {
                'techniques_used': techniques_used,
                'technique_count': len(techniques_used)
            }
        }
    
    def _evaluate_reading_level(self, prompt: str) -> Dict[str, Any]:
        """Evaluate reading level appropriateness"""
        try:
            reading_ease = flesch_reading_ease(prompt)
            grade_level = flesch_kincaid_grade(prompt)
            
            # Score based on appropriate reading level for technical content
            if 30 <= reading_ease <= 60:  # Somewhat difficult to difficult
                score = 1.0
                feedback = "Excellent: Appropriate reading level for technical content"
            elif 20 <= reading_ease <= 70:
                score = 0.8
                feedback = "Good: Reading level is acceptable"
            else:
                score = 0.6
                feedback = "Consider adjusting complexity for better accessibility"
            
            return {
                'score': score,
                'feedback': feedback,
                'details': {
                    'reading_ease': reading_ease,
                    'grade_level': grade_level
                }
            }
        except:
            return {
                'score': 0.5,
                'feedback': "Could not evaluate reading level",
                'details': {}
            }


# Example usage and testing
if __name__ == "__main__":
    # Test Quiz Grader
    quiz_config = {
        'questions': [
            {
                'id': 'q1',
                'type': 'multiple_choice_single',
                'points': 2,
                'correct_answer': 'b',
                'explanation': 'This is the correct answer because...'
            },
            {
                'id': 'q2',
                'type': 'true_false',
                'points': 1,
                'correct_answer': True,
                'explanation': 'This statement is true because...'
            }
        ]
    }
    
    quiz_submission = {
        'answers': {
            'q1': 'b',
            'q2': True
        }
    }
    
    quiz_grader = QuizGrader(quiz_config)
    quiz_result = quiz_grader.grade(quiz_submission)
    
    print("Quiz Grading Result:")
    print(f"Score: {quiz_result.score}/{quiz_result.max_score} ({quiz_result.percentage:.1f}%)")
    print(f"Feedback: {quiz_result.feedback}")
    print(f"Details: {quiz_result.details}")
    
    # Test Prompt Grader
    prompt_config = {
        'evaluation_criteria': {
            'token_efficiency': {'weight': 1.0, 'max_points': 20},
            'clarity': {'weight': 1.0, 'max_points': 20},
            'techniques': {'weight': 1.0, 'max_points': 20}
        }
    }
    
    prompt_submission = {
        'prompt': 'You are a helpful assistant. Please explain the concept of machine learning in simple terms with examples.',
        'expected_output': 'Machine learning is a way for computers to learn patterns from data...',
        'actual_output': 'Machine learning allows computers to learn from data without being explicitly programmed...'
    }
    
    prompt_grader = PromptGrader(prompt_config)
    prompt_result = prompt_grader.grade(prompt_submission)
    
    print("\nPrompt Grading Result:")
    print(f"Score: {prompt_result.score:.1f}/{prompt_result.max_score:.1f} ({prompt_result.percentage:.1f}%)")
    print(f"Feedback: {prompt_result.feedback}")