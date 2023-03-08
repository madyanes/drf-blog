from django.urls import include, path
from rest_framework import routers
from post import views


router = routers.DefaultRouter()
router.register(r'posts', views.PostModelViewSet, basename='post')
