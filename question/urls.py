from rest_framework import routers
from question import views

router = routers.DefaultRouter()
router.register('', viewset=views.QuestionViewSet)

urlpatterns = router.urls
