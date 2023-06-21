from rest_framework import serializers
from grade.models import AnswerGrade, AnswerConfidence


class AnswerGradeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnswerGrade
        fields = [
            'answer',
            'total_grade',
            'created_at',
            'updated_at',
        ]


class AnswerConfidenceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnswerConfidence
        fields = [
            'answer_grade',
            'key_phrase',
            'confidence',
            'grade',
            'created_at',
            'updated_at',
        ]
