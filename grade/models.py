from django.db import models
from abstract_models import timestamp
from model_answer.models import KeyPhrase
from student_answer.models import Answer


class AnswerGrade(timestamp.TimeStamp):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    total_grade = models.FloatField()


class AnswerConfidence(timestamp.TimeStamp):
    answer_grade = models.ForeignKey(AnswerGrade, on_delete=models.CASCADE)
    key_phrase = models.ForeignKey(KeyPhrase, on_delete=models.CASCADE)
    confidence = models.FloatField()
    grade = models.FloatField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['answer_grade', 'key_phrase'],
                name='unique_answer_grade_and_key_phrase_together'
            )
        ]

