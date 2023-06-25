from rest_framework import routers
from model_answer import views

router = routers.DefaultRouter()
router.register('key-phrase', viewset=views.KeyPhraseViewSet)
router.register('', viewset=views.ModelAnswerViewSet)

urlpatterns = router.urls
