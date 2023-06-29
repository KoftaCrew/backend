from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import routers
import auth.views as views

router = routers.DefaultRouter()
router.register('profile', views.UserProfileView)
router.register('sign-up', views.CreateUserView)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh-token/', TokenRefreshView.as_view()),
    path('', include(router.urls))
]
