from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# First we have to register the viewset router before we add to urlpatterns
router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)


urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls)),
]