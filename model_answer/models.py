from question.models import Question
from django.db import models
from abstract_models import timestamp


class ModelAnswer(timestamp.TimeStamp):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=2048)


class KeyPhrase(timestamp.TimeStamp):
    model_answer = models.ForeignKey(ModelAnswer, on_delete=models.CASCADE)
    text = models.CharField(max_length=2048)
