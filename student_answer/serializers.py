from rest_framework import serializers
from student_answer.models import UserAnswer, Answer


class UserAnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserAnswer
        fields = [
            'exam',
            'created_at',
            'updated_at',
        ]


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answer
        fields = [
            'user_answer',
            'question',
            'text',
            'created_at',
            'updated_at',
        ]
