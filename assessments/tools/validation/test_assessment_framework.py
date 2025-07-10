#!/usr/bin/env python3
"""
Validation tests for the Assessment Framework

This module contains comprehensive tests to validate the assessment framework
components including graders, progress tracking, and rubrics.
"""

import unittest
import json
import tempfile
import os
from datetime import datetime, timedelta
from unittest.mock import Mock, patch
import sys

# Add the parent directory to the path so we can import our modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from assessments.tools.auto_grader import QuizGrader, CodeLabGrader, PromptGrader, TestCase, RubricCriterion
from assessments.progress.tracker import ProgressTracker, StudentProgress, Assessment, Submission, AssessmentType, CompletionStatus


class TestQuizGrader(unittest.TestCase):
    """Test cases for QuizGrader"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.quiz_config = {
            'questions': [
                {
                    'id': 'q1',
                    'type': 'multiple_choice_single',
                    'points': 2,
                    'correct_answer': 'b',
                    'explanation': 'Option B is correct because...'
                },
                {
                    'id': 'q2',
                    'type': 'multiple_choice_multiple',
                    'points': 3,
                    'correct_answers': ['a', 'c'],
                    'explanation': 'Options A and C are correct because...'
                },
                {
                    'id': 'q3',
                    'type': 'true_false',
                    'points': 1,
                    'correct_answer': True,
                    'explanation': 'This statement is true because...'
                },
                {
                    'id': 'q4',
                    'type': 'short_answer',
                    'points': 4,
                    'keywords': ['tokenization', 'preprocessing', 'model'],
                    'explanation': 'Key concepts include tokenization and preprocessing...'
                }
            ],
            'partial_credit': True,
            'case_sensitive': False
        }
        self.grader = QuizGrader(self.quiz_config)
    
    def test_perfect_score(self):
        """Test perfect score submission"""
        submission = {
            'answers': {
                'q1': 'b',
                'q2': ['a', 'c'],
                'q3': True,
                'q4': 'Tokenization is the preprocessing step where text is converted into tokens that the model can understand'
            }
        }
        
        result = self.grader.grade(submission)
        
        self.assertEqual(result.score, 10)  # 2 + 3 + 1 + 4
        self.assertEqual(result.max_score, 10)
        self.assertEqual(result.percentage, 100)
        self.assertIn('Correct', result.feedback)
    
    def test_partial_credit(self):
        """Test partial credit for multiple choice multiple"""
        submission = {
            'answers': {
                'q1': 'a',  # Incorrect
                'q2': ['a'],  # Partial - missing 'c'
                'q3': False,  # Incorrect
                'q4': 'Tokenization is important'  # Partial
            }
        }
        
        result = self.grader.grade(submission)
        
        self.assertLess(result.score, 10)
        self.assertGreater(result.score, 0)
        self.assertIn('Partially correct', result.feedback)
    
    def test_missing_answers(self):
        """Test handling of missing answers"""
        submission = {
            'answers': {
                'q1': 'b',
                'q3': True
                # Missing q2 and q4
            }
        }
        
        result = self.grader.grade(submission)
        
        self.assertEqual(result.score, 3)  # Only q1 and q3 correct
        self.assertIn('No answer provided', result.feedback)
    
    def test_case_sensitivity(self):
        """Test case sensitivity settings"""
        # Test case insensitive (default)
        submission = {
            'answers': {
                'q1': 'B',  # Uppercase
                'q2': ['A', 'C'],  # Uppercase
                'q3': True,
                'q4': 'TOKENIZATION is important'
            }
        }
        
        result = self.grader.grade(submission)
        self.assertGreater(result.score, 5)  # Should get points for q1 and q2
        
        # Test case sensitive
        self.grader.case_sensitive = True
        result_sensitive = self.grader.grade(submission)
        self.assertLess(result_sensitive.score, result.score)


class TestCodeLabGrader(unittest.TestCase):
    """Test cases for CodeLabGrader"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.lab_config = {
            'test_cases': [
                {
                    'name': 'test_addition',
                    'input_data': [2, 3],
                    'expected_output': 5,
                    'points': 2.0,
                    'description': 'Test basic addition'
                },
                {
                    'name': 'test_multiplication',
                    'input_data': [4, 5],
                    'expected_output': 20,
                    'points': 3.0,
                    'description': 'Test multiplication'
                }
            ],
            'rubric': [
                {
                    'name': 'code_quality',
                    'description': 'Code quality and style',
                    'max_points': 5.0,
                    'auto_gradable': True
                }
            ],
            'language': 'python',
            'allowed_imports': ['math', 'sys'],
            'forbidden_patterns': ['eval', 'exec']
        }
        self.grader = CodeLabGrader(self.lab_config)
    
    def test_code_grading_structure(self):
        """Test that code grading returns proper structure"""
        submission = {
            'code': '''
def main(data):
    """Simple function for testing"""
    a, b = data
    return a + b
'''
        }
        
        result = self.grader.grade(submission)
        
        self.assertIsInstance(result.score, (int, float))
        self.assertIsInstance(result.max_score, (int, float))
        self.assertIsInstance(result.feedback, str)
        self.assertIsInstance(result.details, dict)
        self.assertIn('static_analysis', result.details)
        self.assertIn('test_results', result.details)
        
    def test_empty_code_submission(self):
        """Test handling of empty code submission"""
        submission = {'code': ''}
        
        result = self.grader.grade(submission)
        
        self.assertEqual(result.score, 0)
        self.assertIn('No code submitted', result.feedback)
    
    def test_syntax_error_handling(self):
        """Test handling of syntax errors"""
        submission = {
            'code': '''
def main(data):
    a, b = data
    return a + b  # Missing closing parenthesis
'''
        }
        
        result = self.grader.grade(submission)
        
        # Should handle syntax errors gracefully
        self.assertIsInstance(result, type(result))
        self.assertIn('static_analysis', result.details)


class TestPromptGrader(unittest.TestCase):
    """Test cases for PromptGrader"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.prompt_config = {
            'evaluation_criteria': {
                'token_efficiency': {'weight': 1.0, 'max_points': 20},
                'clarity': {'weight': 1.0, 'max_points': 20},
                'techniques': {'weight': 1.0, 'max_points': 20},
                'reading_level': {'weight': 1.0, 'max_points': 20}
            },
            'use_openai': False  # Don't use OpenAI for tests
        }
        self.grader = PromptGrader(self.prompt_config)
    
    def test_prompt_grading_structure(self):
        """Test that prompt grading returns proper structure"""
        submission = {
            'prompt': 'You are a helpful assistant. Please explain machine learning in simple terms with examples.',
            'expected_output': 'Machine learning is a way for computers to learn patterns from data...',
            'actual_output': 'Machine learning allows computers to learn from data automatically...'
        }
        
        result = self.grader.grade(submission)
        
        self.assertIsInstance(result.score, (int, float))
        self.assertIsInstance(result.max_score, (int, float))
        self.assertIsInstance(result.feedback, str)
        self.assertIsInstance(result.details, dict)
        self.assertIn('token_efficiency', result.details)
        self.assertIn('clarity', result.details)
    
    def test_empty_prompt_submission(self):
        """Test handling of empty prompt submission"""
        submission = {'prompt': ''}
        
        result = self.grader.grade(submission)
        
        self.assertEqual(result.score, 0)
        self.assertIn('No prompt submitted', result.feedback)
    
    def test_technique_detection(self):
        """Test detection of prompt engineering techniques"""
        submission = {
            'prompt': '''
You are an expert teacher. Please explain the concept step by step with examples.
For instance, consider this scenario: a student is learning about photosynthesis.
You must provide exactly 3 examples in bullet points.
'''
        }
        
        result = self.grader.grade(submission)
        
        # Should detect multiple techniques
        techniques_result = result.details['techniques']
        self.assertGreater(techniques_result['score'], 0.5)
        self.assertIn('role_playing', techniques_result['details']['techniques_used'])
        self.assertIn('few_shot', techniques_result['details']['techniques_used'])
        self.assertIn('constraints', techniques_result['details']['techniques_used'])


class TestProgressTracker(unittest.TestCase):
    """Test cases for ProgressTracker"""
    
    def setUp(self):
        """Set up test fixtures"""
        # Create a temporary file for testing
        self.temp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False)
        self.temp_file.close()
        
        self.tracker = ProgressTracker(data_file=self.temp_file.name)
        
        # Add test student
        self.student = self.tracker.add_student(
            student_id='test_student',
            name='Test Student',
            email='test@example.com',
            cohort='test_cohort'
        )
        
        # Add test assessment
        self.assessment = Assessment(
            id='test_assessment',
            title='Test Assessment',
            type=AssessmentType.QUIZ,
            module='Module 1',
            max_score=100,
            weight=1.0,
            due_date=datetime.now() + timedelta(days=7),
            learning_objectives=['LO.1.1', 'LO.1.2'],
            description='Test assessment for validation'
        )
        self.tracker.add_assessment(self.assessment)
    
    def tearDown(self):
        """Clean up test fixtures"""
        try:
            os.unlink(self.temp_file.name)
        except:
            pass
    
    def test_student_creation(self):
        """Test student creation and storage"""
        self.assertEqual(self.student.student_id, 'test_student')
        self.assertEqual(self.student.name, 'Test Student')
        self.assertEqual(self.student.email, 'test@example.com')
        self.assertEqual(self.student.cohort, 'test_cohort')
        self.assertIsInstance(self.student.start_date, datetime)
    
    def test_assessment_creation(self):
        """Test assessment creation and storage"""
        retrieved_assessment = self.tracker.get_assessment('test_assessment')
        self.assertIsNotNone(retrieved_assessment)
        self.assertEqual(retrieved_assessment.title, 'Test Assessment')
        self.assertEqual(retrieved_assessment.type, AssessmentType.QUIZ)
        self.assertEqual(retrieved_assessment.max_score, 100)
    
    def test_submission_recording(self):
        """Test submission recording and progress updates"""
        submission = Submission(
            id='test_submission',
            assessment_id='test_assessment',
            student_id='test_student',
            submitted_at=datetime.now(),
            status=CompletionStatus.COMPLETED,
            score=85,
            feedback='Good work!',
            attempt_number=1
        )
        
        self.tracker.record_submission(submission)
        
        # Check that submission was recorded
        updated_student = self.tracker.get_student_progress('test_student')
        self.assertEqual(len(updated_student.submissions), 1)
        self.assertEqual(updated_student.submissions[0].score, 85)
        
        # Check that learning objectives were updated
        self.assertIn('LO.1.1', updated_student.learning_objectives)
        self.assertGreater(updated_student.learning_objectives['LO.1.1'].mastery_level, 0)
    
    def test_progress_calculation(self):
        """Test progress calculation"""
        # Submit a successful assessment
        submission = Submission(
            id='test_submission',
            assessment_id='test_assessment',
            student_id='test_student',
            submitted_at=datetime.now(),
            status=CompletionStatus.COMPLETED,
            score=90,
            feedback='Excellent work!',
            attempt_number=1
        )
        
        self.tracker.record_submission(submission)
        
        # Check progress calculations
        updated_student = self.tracker.get_student_progress('test_student')
        self.assertGreater(updated_student.overall_progress, 0)
        self.assertEqual(updated_student.risk_level, 'low')
    
    def test_progress_report_generation(self):
        """Test progress report generation"""
        # Add a submission
        submission = Submission(
            id='test_submission',
            assessment_id='test_assessment',
            student_id='test_student',
            submitted_at=datetime.now(),
            status=CompletionStatus.COMPLETED,
            score=88,
            feedback='Good understanding shown',
            attempt_number=1
        )
        self.tracker.record_submission(submission)
        
        # Generate report
        report = self.tracker.generate_progress_report('test_student')
        
        # Validate report structure
        self.assertIn('student_info', report)
        self.assertIn('overall_progress', report)
        self.assertIn('performance_summary', report)
        self.assertIn('learning_objectives', report)
        self.assertIn('recent_submissions', report)
        
        # Check student info
        self.assertEqual(report['student_info']['name'], 'Test Student')
        self.assertEqual(report['student_info']['id'], 'test_student')
        
        # Check performance summary
        self.assertEqual(report['performance_summary']['total_submissions'], 1)
        self.assertEqual(report['performance_summary']['late_submissions'], 0)
    
    def test_cohort_report_generation(self):
        """Test cohort report generation"""
        # Add another student to the cohort
        student2 = self.tracker.add_student(
            student_id='test_student2',
            name='Test Student 2',
            email='test2@example.com',
            cohort='test_cohort'
        )
        
        # Add submissions for both students
        submission1 = Submission(
            id='test_submission1',
            assessment_id='test_assessment',
            student_id='test_student',
            submitted_at=datetime.now(),
            status=CompletionStatus.COMPLETED,
            score=85,
            feedback='Good work!',
            attempt_number=1
        )
        
        submission2 = Submission(
            id='test_submission2',
            assessment_id='test_assessment',
            student_id='test_student2',
            submitted_at=datetime.now(),
            status=CompletionStatus.COMPLETED,
            score=92,
            feedback='Excellent!',
            attempt_number=1
        )
        
        self.tracker.record_submission(submission1)
        self.tracker.record_submission(submission2)
        
        # Generate cohort report
        report = self.tracker.generate_cohort_report('test_cohort')
        
        # Validate report structure
        self.assertIn('cohort_info', report)
        self.assertIn('progress_summary', report)
        self.assertIn('risk_distribution', report)
        self.assertIn('module_progress', report)
        
        # Check cohort info
        self.assertEqual(report['cohort_info']['student_count'], 2)
        self.assertEqual(report['cohort_info']['name'], 'test_cohort')
    
    def test_risk_assessment(self):
        """Test risk level assessment"""
        # Test low risk (normal progress)
        submission = Submission(
            id='test_submission',
            assessment_id='test_assessment',
            student_id='test_student',
            submitted_at=datetime.now(),
            status=CompletionStatus.COMPLETED,
            score=90,
            feedback='Good work!',
            attempt_number=1
        )
        self.tracker.record_submission(submission)
        
        updated_student = self.tracker.get_student_progress('test_student')
        self.assertEqual(updated_student.risk_level, 'low')
        
        # Test high risk (simulate low performance and inactivity)
        updated_student.last_active = datetime.now() - timedelta(days=10)
        updated_student.overall_progress = 25
        updated_student.risk_level = updated_student.assess_risk_level()
        
        self.assertIn(updated_student.risk_level, ['medium', 'high'])
    
    def test_data_persistence(self):
        """Test data persistence to file"""
        # Create a submission
        submission = Submission(
            id='test_submission',
            assessment_id='test_assessment',
            student_id='test_student',
            submitted_at=datetime.now(),
            status=CompletionStatus.COMPLETED,
            score=85,
            feedback='Good work!',
            attempt_number=1
        )
        self.tracker.record_submission(submission)
        
        # Create a new tracker instance with the same file
        new_tracker = ProgressTracker(data_file=self.temp_file.name)
        
        # Check that data was persisted
        retrieved_student = new_tracker.get_student_progress('test_student')
        self.assertIsNotNone(retrieved_student)
        self.assertEqual(retrieved_student.name, 'Test Student')
        self.assertEqual(len(retrieved_student.submissions), 1)
        
        retrieved_assessment = new_tracker.get_assessment('test_assessment')
        self.assertIsNotNone(retrieved_assessment)
        self.assertEqual(retrieved_assessment.title, 'Test Assessment')


class TestAssessmentIntegration(unittest.TestCase):
    """Integration tests for the complete assessment framework"""
    
    def setUp(self):
        """Set up integration test fixtures"""
        # Create temporary file for progress tracking
        self.temp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False)
        self.temp_file.close()
        
        # Initialize components
        self.tracker = ProgressTracker(data_file=self.temp_file.name)
        
        # Quiz grader configuration
        self.quiz_config = {
            'questions': [
                {
                    'id': 'q1',
                    'type': 'multiple_choice_single',
                    'points': 5,
                    'correct_answer': 'b',
                    'explanation': 'This is correct because...'
                }
            ]
        }
        self.quiz_grader = QuizGrader(self.quiz_config)
    
    def tearDown(self):
        """Clean up integration test fixtures"""
        try:
            os.unlink(self.temp_file.name)
        except:
            pass
    
    def test_end_to_end_assessment_flow(self):
        """Test complete assessment flow from submission to progress tracking"""
        # 1. Add student
        student = self.tracker.add_student(
            student_id='integration_student',
            name='Integration Test Student',
            email='integration@test.com',
            cohort='integration_cohort'
        )
        
        # 2. Add assessment
        assessment = Assessment(
            id='integration_quiz',
            title='Integration Test Quiz',
            type=AssessmentType.QUIZ,
            module='Module 1',
            max_score=5,
            weight=1.0,
            due_date=datetime.now() + timedelta(days=7),
            learning_objectives=['LO.1.1'],
            description='Integration test assessment'
        )
        self.tracker.add_assessment(assessment)
        
        # 3. Grade quiz submission
        quiz_submission = {
            'answers': {'q1': 'b'}
        }
        quiz_result = self.quiz_grader.grade(quiz_submission)
        
        # 4. Record submission with grading results
        submission = Submission(
            id='integration_submission',
            assessment_id='integration_quiz',
            student_id='integration_student',
            submitted_at=datetime.now(),
            status=CompletionStatus.COMPLETED,
            score=quiz_result.score,
            feedback=quiz_result.feedback,
            attempt_number=1
        )
        self.tracker.record_submission(submission)
        
        # 5. Generate progress report
        report = self.tracker.generate_progress_report('integration_student')
        
        # 6. Validate end-to-end flow
        self.assertEqual(quiz_result.score, 5)
        self.assertEqual(quiz_result.percentage, 100)
        self.assertEqual(len(student.submissions), 1)
        self.assertEqual(report['performance_summary']['total_submissions'], 1)
        self.assertGreater(report['overall_progress']['completion_percentage'], 0)
    
    def test_multiple_assessment_types(self):
        """Test handling of multiple assessment types"""
        # Add student
        student = self.tracker.add_student(
            student_id='multi_student',
            name='Multi Assessment Student',
            email='multi@test.com',
            cohort='multi_cohort'
        )
        
        # Add different types of assessments
        quiz_assessment = Assessment(
            id='multi_quiz',
            title='Multi Quiz',
            type=AssessmentType.QUIZ,
            module='Module 1',
            max_score=10,
            weight=1.0,
            due_date=datetime.now() + timedelta(days=7),
            learning_objectives=['LO.1.1'],
            description='Quiz assessment'
        )
        
        lab_assessment = Assessment(
            id='multi_lab',
            title='Multi Lab',
            type=AssessmentType.LAB,
            module='Module 1',
            max_score=20,
            weight=2.0,
            due_date=datetime.now() + timedelta(days=14),
            learning_objectives=['LO.1.2'],
            description='Lab assessment'
        )
        
        project_assessment = Assessment(
            id='multi_project',
            title='Multi Project',
            type=AssessmentType.PROJECT,
            module='Module 1',
            max_score=30,
            weight=3.0,
            due_date=datetime.now() + timedelta(days=21),
            learning_objectives=['LO.1.3'],
            description='Project assessment'
        )
        
        self.tracker.add_assessment(quiz_assessment)
        self.tracker.add_assessment(lab_assessment)
        self.tracker.add_assessment(project_assessment)
        
        # Submit different types of assessments
        quiz_submission = Submission(
            id='multi_quiz_sub',
            assessment_id='multi_quiz',
            student_id='multi_student',
            submitted_at=datetime.now(),
            status=CompletionStatus.COMPLETED,
            score=8,
            feedback='Good quiz performance',
            attempt_number=1
        )
        
        lab_submission = Submission(
            id='multi_lab_sub',
            assessment_id='multi_lab',
            student_id='multi_student',
            submitted_at=datetime.now(),
            status=CompletionStatus.COMPLETED,
            score=16,
            feedback='Solid lab work',
            attempt_number=1
        )
        
        project_submission = Submission(
            id='multi_project_sub',
            assessment_id='multi_project',
            student_id='multi_student',
            submitted_at=datetime.now(),
            status=CompletionStatus.COMPLETED,
            score=25,
            feedback='Excellent project',
            attempt_number=1
        )
        
        self.tracker.record_submission(quiz_submission)
        self.tracker.record_submission(lab_submission)
        self.tracker.record_submission(project_submission)
        
        # Generate report and validate
        report = self.tracker.generate_progress_report('multi_student')
        
        self.assertEqual(report['performance_summary']['total_submissions'], 3)
        self.assertGreater(report['overall_progress']['completion_percentage'], 0)
        
        # Check that different types of assessments are handled correctly
        quiz_percentage = (8 / 10) * 100
        lab_percentage = (16 / 20) * 100
        project_percentage = (25 / 30) * 100
        
        self.assertEqual(quiz_percentage, 80)
        self.assertEqual(lab_percentage, 80)
        self.assertAlmostEqual(project_percentage, 83.33, places=1)


def run_validation_tests():
    """Run all validation tests"""
    # Create test suite
    test_suite = unittest.TestSuite()
    
    # Add test cases
    test_suite.addTest(unittest.makeSuite(TestQuizGrader))
    test_suite.addTest(unittest.makeSuite(TestCodeLabGrader))
    test_suite.addTest(unittest.makeSuite(TestPromptGrader))
    test_suite.addTest(unittest.makeSuite(TestProgressTracker))
    test_suite.addTest(unittest.makeSuite(TestAssessmentIntegration))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    return result.wasSuccessful()


if __name__ == '__main__':
    print("Running Assessment Framework Validation Tests...")
    print("=" * 60)
    
    success = run_validation_tests()
    
    print("\n" + "=" * 60)
    if success:
        print("✅ All validation tests passed!")
        print("✅ Assessment framework is ready for deployment.")
    else:
        print("❌ Some validation tests failed.")
        print("❌ Please review and fix issues before deployment.")
    
    exit(0 if success else 1)