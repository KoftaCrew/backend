from rest_framework import serializers
from exam.models import Exam
from question.serializers import QuestionSerializer


class ExamSerializer(serializers.ModelSerializer):
    exam_questions = QuestionSerializer(many=True)

    class Meta:
        model = Exam
        fields = '__all__'
