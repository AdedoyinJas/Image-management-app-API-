from django.urls import path 
from . import views
from django.urls.conf import include
from rest_framework import routers



router = routers.DefaultRouter()
router.register(r'images' , views.ImageViewSet , basename= 'images')

urlpatterns = [
    path('' , include(router.urls))
]
