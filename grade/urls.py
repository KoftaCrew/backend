from rest_framework import routers
from grade.views import StartGradingTriggerViewSet

router = routers.DefaultRouter()
router.register('', StartGradingTriggerViewSet)

urlpatterns = router.urls
