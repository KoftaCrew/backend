from rest_framework import serializers
from exam.models import Exam


class ExamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Exam
        fields = [
            'id',
            'name',
            'created_at',
            'updated_at',
        ]
