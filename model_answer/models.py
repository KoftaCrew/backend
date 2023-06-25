from question.models import Question
from django.db import models
from abstract_models import timestamp


class ModelAnswer(timestamp.TimeStamp):
    question = models.OneToOneField(
        Question, on_delete=models.CASCADE,
        to_field='id',
        related_name="question_model_answer"
    )
    text = models.CharField(max_length=2048)


class KeyPhrase(timestamp.TimeStamp):
    model_answer = models.ForeignKey(ModelAnswer, on_delete=models.CASCADE, related_name="model_answer_key_phrases")
    start_index = models.IntegerField(null=True)
    end_index = models.IntegerField(null=True)
    grade = models.FloatField(default=0)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(
                    end_index__gt=models.F("start_index")
                ),
                name="end_index_gt_start_index"
            ),
        ]
