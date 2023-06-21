from django.db import models
from abstract_models import timestamp


class Exam(timestamp.TimeStamp):
    name = models.CharField(max_length=255)
