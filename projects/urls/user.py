# from rest_framework.routers import DefaultRouter
from projects.views.user import UserViewSet, UserListGenericView, UserRegisterGenericAPIView
from django.urls import path

# router = DefaultRouter()
# router.register('', UserViewSet, basename='users')

urlpatterns = [
    path("", UserListGenericView.as_view()),
    path("register/", UserRegisterGenericAPIView.as_view()),
]

# urlpatterns += router.urls
