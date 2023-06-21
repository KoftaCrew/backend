from django.urls import path
from rest_framework import routers
from exam import views

router = routers.DefaultRouter()
router.register('', viewset=views.ExamViewSet)

urlpatterns = router.urls