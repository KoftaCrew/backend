from rest_framework import serializers
from exam.models import Exam
from question.serializers import QuestionSerializer


class ExamSerializer(serializers.ModelSerializer):
    exam_questions = QuestionSerializer(
        many=True,
        read_only=True
    )
    user = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Exam
        fields = '__all__'
