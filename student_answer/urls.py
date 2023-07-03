from rest_framework import routers
from student_answer.views import StudentAnswerViewSet, UpdateStudentAnswerViewSet, ResultsViewSet
from django.urls import path, include


router = routers.DefaultRouter()
router.register('student', StudentAnswerViewSet)
router.register('submit', UpdateStudentAnswerViewSet)
router.register('result', ResultsViewSet)

urlpatterns = [
    path('', include(router.urls))
]
