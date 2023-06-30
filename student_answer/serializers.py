from rest_framework import serializers
from django.db import transaction
from django.core.exceptions import ValidationError

from student_answer.models import StudentAnswer, Answer


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'question', 'text', 'created_at', 'updated_at')


class StudentAnswerSerializer(serializers.ModelSerializer):
    student_answer = AnswerSerializer(
        many=True,
        required=False,
        read_only=True
    )

    class Meta:
        model = StudentAnswer
        # optional_fields = ['student_answer']
        fields = [
            'id',
            'exam',
            'student_id',
            'student_name',
            'student_answer',
            'created_at',
            'updated_at',
        ]


class UpdateStudentAnswerSerializer(serializers.ModelSerializer):
    student_answer = AnswerSerializer(
        many=True,
        required=False
    )

    class Meta:
        model = StudentAnswer
        fields = '__all__'

    @transaction.atomic
    def update(self, instance: StudentAnswer, validated_data: dict) -> StudentAnswer:
        instance.student_answer_id.all().delete()
        for question in validated_data.get('student_answer'):
            if question.get('question').exam_id != instance.exam_id:
                raise ValidationError(
                    f"The question id {question.question} doesn't belong to the exam you are currently answering"
                )
            instance.student_answer_id.create(**question)
        return instance
