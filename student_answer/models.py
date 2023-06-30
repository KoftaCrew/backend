from django.db import models
from abstract_models import timestamp
from exam.models import Exam
from question.models import Question


class StudentAnswer(timestamp.TimeStamp):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=32)
    student_name = models.CharField(max_length=128)

    class Meta:
        unique_together = ('exam', 'student_id',)


class Answer(timestamp.TimeStamp):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    student_answer = models.ForeignKey(StudentAnswer, on_delete=models.CASCADE, null=True, related_name='student_answer')
    text = models.CharField(max_length=2048)
