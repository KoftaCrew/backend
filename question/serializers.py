from rest_framework import serializers
from question.models import Question


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = [
            'exam',
            'question',
            'created_at',
            'updated_at',
        ]
