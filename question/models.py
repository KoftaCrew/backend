from django.db import models
from abstract_models import timestamp
from exam.models import Exam


class Question(timestamp.TimeStamp):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name="exam_questions")
    question = models.CharField(max_length=1024)
