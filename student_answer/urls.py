from rest_framework import routers
from student_answer.views import StudentAnswerViewSet, AnswerViewSet
from django.urls import path, include


router = routers.DefaultRouter()
router.register('student', StudentAnswerViewSet)
router.register('answer', AnswerViewSet)

urlpatterns = [
    path('', include(router.urls))
]
