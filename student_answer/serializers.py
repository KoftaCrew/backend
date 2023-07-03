from rest_framework import serializers
from django.db import transaction
from django.core.exceptions import ValidationError

from grade.serializers import AnswerSegmentSerializer
from question.serializers import QuestionSerializer
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

    def create(self, validated_data: dict) -> StudentAnswer:
        exam = validated_data.get('exam')
        if exam.mode == 3:
            potential_instances = StudentAnswer.objects.all().filter(
                exam_id=exam.id,
                student_id=validated_data.get('student_id')
            )
            if potential_instances.filter(is_submitted=True).exists():
                raise ValidationError(
                    "You have already submitted your answers for this exam"
                )
            potential_instances = potential_instances.filter(is_submitted=False)
            if potential_instances.exists():
                instance = potential_instances.get()
                return instance
            return super().create(validated_data)
        raise ValidationError("Exam is not in answer mode yet")


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
                    f"The question id {question.get('question').id} doesn't belong to the exam you are currently "
                    f"answering"
                )
            instance.student_answer_id.create(**question)
        instance.is_submitted = True
        instance.save()
        return instance


class AnswerResultSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(many=False)
    answer_segments = AnswerSegmentSerializer(many=True)

    class Meta:
        model = Answer
        fields = '__all__'


class ResultsSerializer(serializers.ModelSerializer):
    answers = AnswerResultSerializer(
        many=True,
        required=False,
        source='student_answer_id'
    )

    class Meta:
        model = StudentAnswer
        fields = '__all__'
