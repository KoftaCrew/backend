from rest_framework import routers
from exam import views

router = routers.DefaultRouter()
router.register('student-view', viewset=views.StudentExamViewSet)
router.register('card', viewset=views.ExamCardViewSet)
router.register('', viewset=views.ExamViewSet)

urlpatterns = router.urls
