from rest_framework import serializers
from .models import Image
from django.db import models
from django.contrib.auth import get_user_model
from rest_framework import serializers
from djoser.serializers import UserSerializer as BaseUserSerializer, UserCreateSerializer as BaseUserCreateSerializer
User = get_user_model()
from django.core.files.storage import default_storage
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
from django.conf import settings
import tempfile
from django_filters import rest_framework as filters


model = load_model("emotionModel.hdf5",compile = False)
def shapePoints(shape):
    coords = np.zeros((68, 2), dtype="int")
    for i in range(0, 68):
        coords[i] = (shape.part(i).x, shape.part(i).y)
    return coords

def rectPoints(rect):
    x = rect.left()
    y = rect.top()
    w = rect.right() - x
    h = rect.bottom() - y
    return (x, y, w, h)


def get_emotion(image):
    frame = imread(image)
    #frame = image
    #print(image)
    detector = dlib.get_frontal_face_detector()
    emotionTargetSize = model.input_shape[1:3]
    faceLandmarks = "shape_predictor_68_face_landmarks.dat"
    predictor = dlib.shape_predictor(faceLandmarks)
     
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rects = detector(grayFrame, 0)
    #print("hellor",rects)
    if len(rects) !=0:
        for rect in rects:
            shape = predictor(grayFrame, rect)
            points = shapePoints(shape)
            (x, y, w, h) = rectPoints(rect)
            grayFace = grayFrame[y:y + h, x:x + w]
            try:
                grayFace = cv2.resize(grayFace, (emotionTargetSize))
            except Exception as exc:
                print(exc)
            grayFace = grayFace.astype('float32')
            grayFace = grayFace / 255.0
            grayFace = (grayFace - 0.5) * 2.0
            grayFace = np.expand_dims(grayFace, 0)
            grayFace = np.expand_dims(grayFace, -1)
            emotion_prediction = model.predict(grayFace,verbose = 0)
            emotion_probability = np.max(emotion_prediction)

            predictions = ["Anrgy","Disgust","Fear","Happy","Sad","Suprised","neutral"]
            result = predictions[emotion_prediction.argmax()]
    else:
        result = ('No emotion')

    return result

class ImageFilter(filters.FilterSet):
    emotion = filters.CharFilter(field_name='emotion' , lookup_expr='iexact')
    
    class Meta:
        model = Image
        fields = ['emotion']

class ImageSerializer(serializers.ModelSerializer):     
    emotion = serializers.SerializerMethodField()
    
    class Meta:
        model = Image
        fields = ('user' , 'first_name' , 'last_name' , 'uploaded_at'  , 'image' , 'emotion')

    
    def get_emotion(self, obj):
        return obj.emotion
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        path = instance.image.path
        emotion = get_emotion(path)
        representation['emotion'] = emotion
        return representation

    



class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'password','email', 'first_name', 'last_name']


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

    
    # def get_emotion(self, obj):
    #     return obj.emotion
    
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     with default_storage.open(instance.image.name) as file:
            
    #         image_content = file.read()

    #     with tempfile.NameTemporaryFile(delete=False) as temp_file:
    #         temp_file.write(image_content)
    #         temp_file.fluush()
    #         temp_file.seek(0)
        
    #         emotion = get_emotion(temp_fie.name)
                                  
    #     representation['emotion'] = emotion
    #     return representation


    # def create(self , validated_data):
    #     image_file_data = validated_data.pop('image')

    #     instance = Image.objects.create(**validated_data)
    #     instance.image.save(image_file_data.name, image_file_data)
    #     #instance = Image(image=image_file_data)

    #     with default_storage.open(instance.image.name) as file:
    #         image_content = file.read()

    #     with tempfile.NameTemporaryFile(delete=False) as temp_file:
    #         temp_file.write(image_content)
    #         temp_file.flush()
    #         temp_file.seek(0)

        
    #         emotion = get_emotion(temp_file.name)
        
    #     instance.emotion = emotion
        
    #     instance.save()

    #     return instance

