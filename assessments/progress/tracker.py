#!/usr/bin/env python3
"""
Progress Tracking System for Prompt Engineering Course

This module provides comprehensive progress tracking capabilities for students
and instructors in the prompt engineering course assessment framework.
"""

import json
import pandas as pd
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass, asdict
from enum import Enum
import uuid


class AssessmentType(Enum):
    """Types of assessments in the course"""
    QUIZ = "quiz"
    LAB = "lab"
    PROJECT = "project"
    PARTICIPATION = "participation"
    REFLECTION = "reflection"
    PEER_REVIEW = "peer_review"
    CAPSTONE = "capstone"


class CompletionStatus(Enum):
    """Assessment completion statuses"""
    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    SUBMITTED = "submitted"
    REVIEWED = "reviewed"
    COMPLETED = "completed"
    LATE = "late"
    RESUBMISSION = "resubmission"


@dataclass
class LearningObjective:
    """Individual learning objective tracking"""
    id: str
    description: str
    module: str
    category: str  # knowledge, application, synthesis, evaluation
    mastery_level: float = 0.0  # 0.0 to 1.0
    evidence_count: int = 0
    last_assessed: Optional[datetime] = None
    
    def update_mastery(self, score: float, weight: float = 1.0):
        """Update mastery level based on new assessment"""
        if self.evidence_count == 0:
            self.mastery_level = score
        else:
            # Weighted average with recency bias
            self.mastery_level = (
                self.mastery_level * self.evidence_count + score * weight
            ) / (self.evidence_count + weight)
        
        self.evidence_count += 1
        self.last_assessed = datetime.now()


@dataclass
class Assessment:
    """Individual assessment record"""
    id: str
    title: str
    type: AssessmentType
    module: str
    max_score: float
    weight: float
    due_date: datetime
    learning_objectives: List[str]
    description: str = ""
    instructions: str = ""
    resources: List[str] = None
    
    def __post_init__(self):
        if self.resources is None:
            self.resources = []


@dataclass
class Submission:
    """Student submission record"""
    id: str
    assessment_id: str
    student_id: str
    submitted_at: datetime
    status: CompletionStatus
    score: Optional[float] = None
    feedback: str = ""
    attempt_number: int = 1
    time_spent: Optional[int] = None  # minutes
    files: List[str] = None
    metadata: Dict[str, Any] = None
    
    def __post_init__(self):
        if self.files is None:
            self.files = []
        if self.metadata is None:
            self.metadata = {}
    
    @property
    def is_late(self) -> bool:
        """Check if submission was late"""
        assessment = ProgressTracker.get_assessment(self.assessment_id)
        return self.submitted_at > assessment.due_date if assessment else False
    
    @property
    def percentage_score(self) -> Optional[float]:
        """Get percentage score"""
        if self.score is None:
            return None
        assessment = ProgressTracker.get_assessment(self.assessment_id)
        return (self.score / assessment.max_score) * 100 if assessment else None


@dataclass
class StudentProgress:
    """Comprehensive student progress tracking"""
    student_id: str
    name: str
    email: str
    cohort: str
    start_date: datetime
    submissions: List[Submission]
    learning_objectives: Dict[str, LearningObjective]
    module_progress: Dict[str, float]  # Module completion percentage
    overall_progress: float = 0.0
    current_module: str = "Module 1"
    risk_level: str = "low"  # low, medium, high
    last_active: Optional[datetime] = None
    notes: str = ""
    
    def __post_init__(self):
        if not self.submissions:
            self.submissions = []
        if not self.learning_objectives:
            self.learning_objectives = {}
        if not self.module_progress:
            self.module_progress = {}
    
    def calculate_module_progress(self, module: str) -> float:
        """Calculate progress for a specific module"""
        module_assessments = ProgressTracker.get_module_assessments(module)
        if not module_assessments:
            return 0.0
        
        completed = sum(
            1 for assessment in module_assessments
            if self.is_assessment_completed(assessment.id)
        )
        return (completed / len(module_assessments)) * 100
    
    def is_assessment_completed(self, assessment_id: str) -> bool:
        """Check if assessment is completed"""
        return any(
            sub.assessment_id == assessment_id and 
            sub.status in [CompletionStatus.COMPLETED, CompletionStatus.REVIEWED]
            for sub in self.submissions
        )
    
    def get_assessment_score(self, assessment_id: str) -> Optional[float]:
        """Get best score for an assessment"""
        relevant_submissions = [
            sub for sub in self.submissions 
            if sub.assessment_id == assessment_id and sub.score is not None
        ]
        return max(sub.score for sub in relevant_submissions) if relevant_submissions else None
    
    def calculate_overall_progress(self) -> float:
        """Calculate overall course progress"""
        if not self.module_progress:
            return 0.0
        
        total_modules = len(self.module_progress)
        if total_modules == 0:
            return 0.0
        
        return sum(self.module_progress.values()) / total_modules
    
    def assess_risk_level(self) -> str:
        """Assess student risk level based on progress and engagement"""
        # Calculate risk factors
        risk_factors = []
        
        # Low overall progress
        if self.overall_progress < 50:
            risk_factors.append("low_progress")
        
        # Recent inactivity
        if self.last_active and (datetime.now() - self.last_active).days > 7:
            risk_factors.append("inactive")
        
        # Low quiz scores
        quiz_scores = [
            sub.percentage_score for sub in self.submissions
            if sub.percentage_score and 
            ProgressTracker.get_assessment(sub.assessment_id).type == AssessmentType.QUIZ
        ]
        if quiz_scores and sum(quiz_scores) / len(quiz_scores) < 70:
            risk_factors.append("low_quiz_performance")
        
        # Missing submissions
        overdue_count = sum(
            1 for sub in self.submissions
            if sub.status == CompletionStatus.LATE
        )
        if overdue_count > 2:
            risk_factors.append("frequent_late_submissions")
        
        # Determine risk level
        if len(risk_factors) >= 3:
            return "high"
        elif len(risk_factors) >= 1:
            return "medium"
        else:
            return "low"


class ProgressTracker:
    """Main progress tracking system"""
    
    def __init__(self, data_file: str = "progress_data.json"):
        self.data_file = data_file
        self.students: Dict[str, StudentProgress] = {}
        self.assessments: Dict[str, Assessment] = {}
        self.course_config = self._load_course_config()
        self._load_data()
    
    def _load_course_config(self) -> Dict:
        """Load course configuration"""
        return {
            "modules": [
                f"Module {i}" for i in range(1, 13)
            ],
            "learning_objectives": self._initialize_learning_objectives(),
            "assessment_weights": {
                AssessmentType.QUIZ: 0.2,
                AssessmentType.LAB: 0.3,
                AssessmentType.PROJECT: 0.3,
                AssessmentType.PARTICIPATION: 0.1,
                AssessmentType.CAPSTONE: 0.1
            }
        }
    
    def _initialize_learning_objectives(self) -> Dict[str, LearningObjective]:
        """Initialize learning objectives for the course"""
        objectives = {}
        
        # Sample learning objectives (would be loaded from configuration)
        for module_num in range(1, 13):
            module = f"Module {module_num}"
            for obj_num in range(1, 5):
                obj_id = f"LO.{module_num}.{obj_num}"
                objectives[obj_id] = LearningObjective(
                    id=obj_id,
                    description=f"Learning objective {obj_num} for {module}",
                    module=module,
                    category="application"  # Would be properly categorized
                )
        
        return objectives
    
    def _load_data(self):
        """Load progress data from file"""
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                
            # Load students
            for student_data in data.get('students', []):
                student = self._deserialize_student(student_data)
                self.students[student.student_id] = student
                
            # Load assessments
            for assessment_data in data.get('assessments', []):
                assessment = self._deserialize_assessment(assessment_data)
                self.assessments[assessment.id] = assessment
                
        except FileNotFoundError:
            # Initialize with empty data
            self.students = {}
            self.assessments = {}
    
    def _save_data(self):
        """Save progress data to file"""
        data = {
            'students': [self._serialize_student(student) for student in self.students.values()],
            'assessments': [self._serialize_assessment(assessment) for assessment in self.assessments.values()],
            'last_updated': datetime.now().isoformat()
        }
        
        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=2, default=str)
    
    def _serialize_student(self, student: StudentProgress) -> Dict:
        """Serialize student progress for JSON storage"""
        return {
            **asdict(student),
            'submissions': [asdict(sub) for sub in student.submissions],
            'learning_objectives': {
                obj_id: asdict(obj) for obj_id, obj in student.learning_objectives.items()
            }
        }
    
    def _deserialize_student(self, data: Dict) -> StudentProgress:
        """Deserialize student progress from JSON data"""
        # Convert string dates back to datetime objects
        if isinstance(data['start_date'], str):
            data['start_date'] = datetime.fromisoformat(data['start_date'])
        if data.get('last_active') and isinstance(data['last_active'], str):
            data['last_active'] = datetime.fromisoformat(data['last_active'])
        
        # Convert submissions
        submissions = []
        for sub_data in data.get('submissions', []):
            if isinstance(sub_data['submitted_at'], str):
                sub_data['submitted_at'] = datetime.fromisoformat(sub_data['submitted_at'])
            sub_data['status'] = CompletionStatus(sub_data['status'])
            submissions.append(Submission(**sub_data))
        
        # Convert learning objectives
        learning_objectives = {}
        for obj_id, obj_data in data.get('learning_objectives', {}).items():
            if obj_data.get('last_assessed') and isinstance(obj_data['last_assessed'], str):
                obj_data['last_assessed'] = datetime.fromisoformat(obj_data['last_assessed'])
            learning_objectives[obj_id] = LearningObjective(**obj_data)
        
        data['submissions'] = submissions
        data['learning_objectives'] = learning_objectives
        
        return StudentProgress(**data)
    
    def _serialize_assessment(self, assessment: Assessment) -> Dict:
        """Serialize assessment for JSON storage"""
        return {
            **asdict(assessment),
            'type': assessment.type.value,
            'due_date': assessment.due_date.isoformat()
        }
    
    def _deserialize_assessment(self, data: Dict) -> Assessment:
        """Deserialize assessment from JSON data"""
        data['type'] = AssessmentType(data['type'])
        data['due_date'] = datetime.fromisoformat(data['due_date'])
        return Assessment(**data)
    
    def add_student(self, student_id: str, name: str, email: str, cohort: str) -> StudentProgress:
        """Add a new student to the tracking system"""
        student = StudentProgress(
            student_id=student_id,
            name=name,
            email=email,
            cohort=cohort,
            start_date=datetime.now(),
            submissions=[],
            learning_objectives=self.course_config['learning_objectives'].copy(),
            module_progress={},
            last_active=datetime.now()
        )
        
        self.students[student_id] = student
        self._save_data()
        return student
    
    def add_assessment(self, assessment: Assessment):
        """Add an assessment to the tracking system"""
        self.assessments[assessment.id] = assessment
        self._save_data()
    
    def record_submission(self, submission: Submission):
        """Record a student submission"""
        student = self.students.get(submission.student_id)
        if not student:
            raise ValueError(f"Student {submission.student_id} not found")
        
        # Update existing submission or add new one
        existing_idx = next(
            (i for i, sub in enumerate(student.submissions) 
             if sub.assessment_id == submission.assessment_id and sub.attempt_number == submission.attempt_number),
            None
        )
        
        if existing_idx is not None:
            student.submissions[existing_idx] = submission
        else:
            student.submissions.append(submission)
        
        # Update learning objectives based on submission
        self._update_learning_objectives(student, submission)
        
        # Update last active
        student.last_active = datetime.now()
        
        # Recalculate progress
        self._update_student_progress(student)
        
        self._save_data()
    
    def _update_learning_objectives(self, student: StudentProgress, submission: Submission):
        """Update learning objectives based on submission"""
        assessment = self.assessments.get(submission.assessment_id)
        if not assessment or submission.score is None:
            return
        
        score_percentage = submission.score / assessment.max_score
        
        # Update each learning objective associated with the assessment
        for obj_id in assessment.learning_objectives:
            if obj_id in student.learning_objectives:
                student.learning_objectives[obj_id].update_mastery(
                    score_percentage,
                    weight=assessment.weight
                )
    
    def _update_student_progress(self, student: StudentProgress):
        """Update student's overall progress metrics"""
        # Update module progress
        for module in self.course_config['modules']:
            student.module_progress[module] = student.calculate_module_progress(module)
        
        # Update overall progress
        student.overall_progress = student.calculate_overall_progress()
        
        # Update risk level
        student.risk_level = student.assess_risk_level()
        
        # Update current module
        for module in self.course_config['modules']:
            if student.module_progress.get(module, 0) < 100:
                student.current_module = module
                break
    
    def get_student_progress(self, student_id: str) -> Optional[StudentProgress]:
        """Get progress for a specific student"""
        return self.students.get(student_id)
    
    def get_assessment(self, assessment_id: str) -> Optional[Assessment]:
        """Get assessment by ID"""
        return self.assessments.get(assessment_id)
    
    @staticmethod
    def get_module_assessments(module: str) -> List[Assessment]:
        """Get all assessments for a module"""
        # This would query the assessments by module
        # For now, return empty list
        return []
    
    def generate_progress_report(self, student_id: str) -> Dict:
        """Generate comprehensive progress report for a student"""
        student = self.students.get(student_id)
        if not student:
            return {}
        
        # Calculate performance metrics
        quiz_scores = [
            sub.percentage_score for sub in student.submissions
            if sub.percentage_score and 
            self.assessments.get(sub.assessment_id, Assessment("", "", AssessmentType.QUIZ, "", 0, 0, datetime.now(), [])).type == AssessmentType.QUIZ
        ]
        
        lab_scores = [
            sub.percentage_score for sub in student.submissions
            if sub.percentage_score and 
            self.assessments.get(sub.assessment_id, Assessment("", "", AssessmentType.LAB, "", 0, 0, datetime.now(), [])).type == AssessmentType.LAB
        ]
        
        project_scores = [
            sub.percentage_score for sub in student.submissions
            if sub.percentage_score and 
            self.assessments.get(sub.assessment_id, Assessment("", "", AssessmentType.PROJECT, "", 0, 0, datetime.now(), [])).type == AssessmentType.PROJECT
        ]
        
        # Generate report
        report = {
            'student_info': {
                'name': student.name,
                'id': student.student_id,
                'cohort': student.cohort,
                'start_date': student.start_date.isoformat(),
                'last_active': student.last_active.isoformat() if student.last_active else None
            },
            'overall_progress': {
                'completion_percentage': student.overall_progress,
                'current_module': student.current_module,
                'risk_level': student.risk_level
            },
            'module_progress': student.module_progress,
            'performance_summary': {
                'quiz_average': sum(quiz_scores) / len(quiz_scores) if quiz_scores else 0,
                'lab_average': sum(lab_scores) / len(lab_scores) if lab_scores else 0,
                'project_average': sum(project_scores) / len(project_scores) if project_scores else 0,
                'total_submissions': len(student.submissions),
                'late_submissions': sum(1 for sub in student.submissions if sub.is_late)
            },
            'learning_objectives': {
                obj_id: {
                    'description': obj.description,
                    'mastery_level': obj.mastery_level,
                    'evidence_count': obj.evidence_count,
                    'last_assessed': obj.last_assessed.isoformat() if obj.last_assessed else None
                }
                for obj_id, obj in student.learning_objectives.items()
            },
            'recent_submissions': [
                {
                    'assessment_id': sub.assessment_id,
                    'assessment_title': self.assessments.get(sub.assessment_id, Assessment("", "Unknown", AssessmentType.QUIZ, "", 0, 0, datetime.now(), [])).title,
                    'submitted_at': sub.submitted_at.isoformat(),
                    'score': sub.score,
                    'percentage': sub.percentage_score,
                    'status': sub.status.value,
                    'attempt_number': sub.attempt_number
                }
                for sub in sorted(student.submissions, key=lambda x: x.submitted_at, reverse=True)[:10]
            ]
        }
        
        return report
    
    def generate_cohort_report(self, cohort: str) -> Dict:
        """Generate cohort-level progress report"""
        cohort_students = [s for s in self.students.values() if s.cohort == cohort]
        
        if not cohort_students:
            return {}
        
        # Calculate cohort statistics
        overall_progress = [s.overall_progress for s in cohort_students]
        risk_levels = [s.risk_level for s in cohort_students]
        
        report = {
            'cohort_info': {
                'name': cohort,
                'student_count': len(cohort_students),
                'report_date': datetime.now().isoformat()
            },
            'progress_summary': {
                'average_progress': sum(overall_progress) / len(overall_progress),
                'min_progress': min(overall_progress),
                'max_progress': max(overall_progress),
                'students_at_risk': sum(1 for risk in risk_levels if risk in ['medium', 'high'])
            },
            'risk_distribution': {
                'low': sum(1 for risk in risk_levels if risk == 'low'),
                'medium': sum(1 for risk in risk_levels if risk == 'medium'),
                'high': sum(1 for risk in risk_levels if risk == 'high')
            },
            'module_progress': {
                module: {
                    'average': sum(s.module_progress.get(module, 0) for s in cohort_students) / len(cohort_students),
                    'completed': sum(1 for s in cohort_students if s.module_progress.get(module, 0) >= 100)
                }
                for module in self.course_config['modules']
            }
        }
        
        return report
    
    def identify_at_risk_students(self, cohort: str = None) -> List[StudentProgress]:
        """Identify students who may need additional support"""
        students = self.students.values()
        if cohort:
            students = [s for s in students if s.cohort == cohort]
        
        return [s for s in students if s.risk_level in ['medium', 'high']]
    
    def get_learning_objective_analytics(self) -> Dict:
        """Analyze learning objective mastery across all students"""
        analytics = {}
        
        for obj_id, obj in self.course_config['learning_objectives'].items():
            student_masteries = []
            for student in self.students.values():
                if obj_id in student.learning_objectives:
                    student_masteries.append(student.learning_objectives[obj_id].mastery_level)
            
            if student_masteries:
                analytics[obj_id] = {
                    'description': obj.description,
                    'module': obj.module,
                    'category': obj.category,
                    'average_mastery': sum(student_masteries) / len(student_masteries),
                    'min_mastery': min(student_masteries),
                    'max_mastery': max(student_masteries),
                    'students_assessed': len(student_masteries),
                    'mastery_distribution': {
                        'excellent': sum(1 for m in student_masteries if m >= 0.9),
                        'good': sum(1 for m in student_masteries if 0.7 <= m < 0.9),
                        'needs_improvement': sum(1 for m in student_masteries if m < 0.7)
                    }
                }
        
        return analytics


# Example usage and testing
if __name__ == "__main__":
    # Initialize tracker
    tracker = ProgressTracker()
    
    # Add sample student
    student = tracker.add_student(
        student_id="student_001",
        name="John Doe",
        email="john.doe@example.com",
        cohort="2025_spring"
    )
    
    # Add sample assessment
    assessment = Assessment(
        id="quiz_001",
        title="Module 1 Knowledge Check",
        type=AssessmentType.QUIZ,
        module="Module 1",
        max_score=100,
        weight=1.0,
        due_date=datetime.now() + timedelta(days=7),
        learning_objectives=["LO.1.1", "LO.1.2", "LO.1.3"],
        description="Knowledge check for Module 1 concepts"
    )
    tracker.add_assessment(assessment)
    
    # Record submission
    submission = Submission(
        id=str(uuid.uuid4()),
        assessment_id="quiz_001",
        student_id="student_001",
        submitted_at=datetime.now(),
        status=CompletionStatus.COMPLETED,
        score=85,
        feedback="Good understanding of core concepts",
        attempt_number=1,
        time_spent=15
    )
    tracker.record_submission(submission)
    
    # Generate progress report
    report = tracker.generate_progress_report("student_001")
    print(json.dumps(report, indent=2, default=str))
    
    # Generate cohort report
    cohort_report = tracker.generate_cohort_report("2025_spring")
    print(json.dumps(cohort_report, indent=2, default=str))