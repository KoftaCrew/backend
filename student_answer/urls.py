from rest_framework import routers
from student_answer.views import StudentAnswerViewSet, UpdateStudentAnswerViewSet
from django.urls import path, include


router = routers.DefaultRouter()
router.register('student', StudentAnswerViewSet)
router.register('submit', UpdateStudentAnswerViewSet)

urlpatterns = [
    path('', include(router.urls))
]
