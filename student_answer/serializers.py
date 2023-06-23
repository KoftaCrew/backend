from rest_framework import serializers
from student_answer.models import UserAnswer, Answer


class UserAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnswer
        fields = [
            'exam',
            'created_at',
            'updated_at',
        ]


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
