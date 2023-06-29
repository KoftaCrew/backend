from django.db import models
from abstract_models import timestamp
from exam.models import Exam
from model_answer.models import ModelAnswer


class Question(timestamp.TimeStamp):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name="exam_questions")
    question = models.CharField(max_length=1024)
    model_answer = models.OneToOneField(
        ModelAnswer, on_delete=models.CASCADE,
        to_field='id',
        null=True
    )
