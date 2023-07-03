from django.db import models
from abstract_models import timestamp
from model_answer.models import KeyPhrase
from student_answer.models import Answer


class AnswerSegment(timestamp.TimeStamp):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=False, related_name='answer_segments')
    key_phrase = models.ForeignKey(KeyPhrase, on_delete=models.CASCADE, null=False)
    start_index = models.IntegerField()
    end_index = models.IntegerField()
    grade = models.FloatField()
    confidence = models.FloatField()

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(
                    end_index__gt=models.F("start_index")
                ),
                name="student_answer_end_index_gt_start_index"
            )
        ]
