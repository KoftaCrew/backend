from rest_framework import serializers
from student_answer.models import StudentAnswer, Answer


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'question', 'text', 'created_at', 'updated_at')


class StudentAnswerSerializer(serializers.ModelSerializer):
    student_answer = AnswerSerializer(
        many=True,
        required=False
    )

    class Meta:
        model = StudentAnswer
        optional_fields = ['student_answer']
        fields = [
            'id',
            'exam',
            'student_id',
            'student_name',
            'student_answer',
            'created_at',
            'updated_at',
        ]
