from rest_framework import serializers
from django.db import transaction

from exam.models import Exam
from question.serializers import QuestionSerializer, StudentQuestionDTOSerializer


def get_mode_update(instance: Exam, new_mode: int | None) -> int | None:
    if new_mode is not None:
        if instance.mode in [0, 1]:
            return new_mode
        if instance.mode == 3 and new_mode == 4:
            return 4
    return instance.mode


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
    def update(self, instance: Exam, validated_data: dict) -> Exam:
        for attr, value in validated_data.items():
            if attr not in ['exam_questions', 'mode']:
                setattr(instance, attr, value)

        new_mode = get_mode_update(instance, validated_data.get('mode'))
        if new_mode is not None:
            instance.mode = new_mode
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

    def update(self, instance: Exam, validated_data: dict) -> Exam:
        for attr, value in validated_data.items():
            if attr not in ['mode']:
                setattr(instance, attr, value)
        new_mode = get_mode_update(instance, validated_data.get('mode'))
        if new_mode is not None:
            instance.mode = new_mode
        instance.save()
        return instance
