from django.db import models
from abstract_models import timestamp
from exam.models import Exam
from question.models import Question


class UserAnswer(timestamp.TimeStamp):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)


class Answer(timestamp.TimeStamp):
    user_answer = models.ForeignKey(UserAnswer, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=2048)
