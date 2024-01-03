from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, permissions
from .models import Image
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny , IsAuthenticated , IsAdminUser 
from .serializers import UserSerializer , ImageSerializer  , ImageFilter
from rest_framework.generics import GenericAPIView
from .pagination import DefaultPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet, GenericViewSet
#from .filters import ImageFilter
from django.http import JsonResponse
#from django.views.decorators.crsf import crsf_exempt
import dlib
import cv2
import numpy as np
from keras.models import load_model
from matplotlib.image import imread
from rest_framework.viewsets import ViewSet 
from rest_framework import viewsets
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO





class ImageViewSet(ModelViewSet):
    permission_classes =  [IsAdminUser]
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    filter_backends = [  DjangoFilterBackend, SearchFilter]
    filter_fields = ImageFilter
    filterset_class = ImageFilter
    pagination_class = DefaultPagination
    search_fields = [ 'uploaded_at' ,'last_name' , 'emotion' ]
       
    def get_permission(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated]
    
    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
    def me(self, request):
        (image , created) = Image.objects.get_or_create(user_id = request.user.id)
        if request.method == 'GET':
            serializer = ImageSerializer(image)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = ImageSerializer(image, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)



                                    












    
