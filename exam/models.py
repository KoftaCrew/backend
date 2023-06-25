from django.db import models
from abstract_models import timestamp
from django.utils.translation import gettext_lazy as _


class Exam(timestamp.TimeStamp):
    class ExamModes(models.IntegerChoices):
        IDLE = 0, _("idle")
        EDITING = 1, _("edit")
        RESULTS = 2, _("result")

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=2048, null=True)
    mode = models.IntegerField(
        choices=ExamModes.choices,
        default=ExamModes.IDLE
    )
