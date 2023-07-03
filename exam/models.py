from django.contrib.auth.models import User
from django.db import models

from abstract_models import timestamp


class Exam(timestamp.TimeStamp):
    class ExamModes(models.IntegerChoices):
        IDLE = 0, "idle"
        EDITING = 1, "edit"
        RESULTS = 2, "result"
        ANSWERING = 3, "answer"
        GRADING = 4, 'grading'

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=2048, null=True)
    mode = models.IntegerField(
        choices=ExamModes.choices,
        default=ExamModes.IDLE
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, to_field='id', null=True)
