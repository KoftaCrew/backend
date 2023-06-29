from rest_framework import serializers
from rest_framework.utils import model_meta

import question.models
from exam.models import Exam
from question.serializers import QuestionSerializer
from django.db import transaction


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
        fields = '__all__'

    @transaction.atomic
    def update(self, instance: Exam, validated_data):
        info = model_meta.get_field_info(instance)

        # Simply set each attribute on the instance, and then save it.
        # Note that unlike `.create()` we don't need to treat many-to-many
        # relationships as being a special case. During updates we already
        # have an instance pk for the relationships to be associated with.
        m2m_fields = []
        for attr, value in validated_data.items():
            if attr in info.relations and info.relations[attr].to_many:
                m2m_fields.append((attr, value))
            else:
                setattr(instance, attr, value)

        instance.save()

        # Note that many-to-many fields are set after updating instance.
        # Setting m2m fields triggers signals which could potentially change
        # updated instance and we do not want it to collide with .update()
        try:
            instance.exam_questions.all().delete()
        finally:
            for attr, values in m2m_fields:
                field = getattr(instance, attr)
                for value in values:
                    field.create(**value)

            return instance

    @transaction.atomic
    def create(self, validated_data: dict)->Exam:
        instance = Exam.objects.create(
            name=validated_data.get('name', None),
            description=validated_data.get('description', None),
            user_id=validated_data.get('user_id', None)
        )
        info = model_meta.get_field_info(instance)
        m2m_fields = []
        for attr, value in validated_data.items():
            if attr in info.relations and info.relations[attr].to_many:
                m2m_fields.append((attr, value))
        for attr, values in m2m_fields:
            field = getattr(instance, attr)
            for value in values:
                field.create(**value, exam=instance.id)
        instance.save()
        return instance


