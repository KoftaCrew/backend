from rest_framework import serializers
from grade.models import AnswerGrade, AnswerConfidence


class AnswerGradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerGrade
        fields = '__all__'


class AnswerConfidenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerConfidence
        fields = '__all__'
