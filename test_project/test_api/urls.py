from django.conf.urls import url, include
from rest_framework import routers
from test_api.views import UserViewSet
from django.urls import path,include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_auth.urls')),   #url for authorization 
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # url for create token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), #url for refresh created token
]
