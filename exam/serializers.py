from rest_framework import serializers
from rest_framework.utils import model_meta
from django.db import transaction

from exam.models import Exam
from question.serializers import QuestionSerializer, StudentQuestionDTOSerializer


class ExamSerializer(serializers.ModelSerializer):
    exam_questions = QuestionSerializer(
        many=True,
    )

    user = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Exam
        depth = 4
        fields = '__all__'

    @transaction.atomic
    def update(self, instance: Exam, validated_data):
        for attr, value in validated_data.items():
            if attr != 'exam_questions':
                setattr(instance, attr, value)

        instance.save()
        question_serializer = QuestionSerializer()
        try:
            instance.exam_questions.all().delete()
        finally:
            for value in self.validated_data.get('exam_questions', []):
                value['exam'] = instance
                QuestionSerializer.create(question_serializer, value)

        return instance

    @transaction.atomic
    def create(self, validated_data: dict) -> Exam:
        instance = Exam.objects.create(
            name=validated_data.get('name', None),
            description=validated_data.get('description', None),
            user_id=validated_data.get('user_id', None)
        )
        question_serializer = QuestionSerializer()
        for value in validated_data.get('exam_questions', []):
            value['exam'] = instance
            QuestionSerializer.create(question_serializer, value)
        instance.save()
        return instance


class StudentExamDTOSerializer(serializers.ModelSerializer):
    exam_questions = StudentQuestionDTOSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Exam
        depth = 2
        fields = ['id', 'name', 'description', 'mode', 'exam_questions']


class ExamCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['id', 'name', 'description', 'mode', 'created_at', 'updated_at']
