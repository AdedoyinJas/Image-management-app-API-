# import dlib
# import numpy as np
# from tensorflow.keras.models import load_model
# from matplotlib.image import imread
# import cv2
# from django.http import JsonResponse
# #from mainapp.views import FacialRecognitionViewSet



# model = load_model("emotionModel.hdf5",compile = False)

# def shapePoints(shape):
#     coords = np.zeros((68, 2), dtype="int")
#     for i in range(0, 68):
#         coords[i] = (shape.part(i).x, shape.part(i).y)
#     return coords


# def rectPoints(rect):
#     x = rect.left()
#     y = rect.top()
#     w = rect.right() - x
#     h = rect.bottom() - y
#     return (x, y, w, h)

# def tell_emotion(image):
#     frame = imread(image)
    
#     detector = dlib.get_frontal_face_detector()
#     emotionTargetSize = model.input_shape[1:3]
#     faceLandmarks = "shape_predictor_68_face_landmarks.dat"
#     predictor = dlib.shape_predictor(faceLandmarks)


    
#     grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     rects = detector(grayFrame, 0)
#     # if len(rects) !=0:
#     for rect in rects:
#         shape = predictor(grayFrame, rect)
#         points = shapePoints(shape)
#         (x, y, w, h) = rectPoints(rect)
#         grayFace = grayFrame[y:y + h, x:x + w]
#         try:
#             grayFace = cv2.resize(grayFace, (emotionTargetSize))
#         except:
#             continue
#         grayFace = grayFace.astype('float32')
#         grayFace = grayFace / 255.0
#         grayFace = (grayFace - 0.5) * 2.0
#         grayFace = np.expand_dims(grayFace, 0)
#         grayFace = np.expand_dims(grayFace, -1)
#         emotion_prediction = model.predict(grayFace,verbose = 0)
#         emotion_probability = np.max(emotion_prediction)

#         predictions = ["Anrgy","Disgust","Fear","Happy","Sad","Suprised","neutral"]

#         emotion = predictions[emotion_prediction.argmax()]
#     else:
#         return emotion

#     # return ("Model cannot detect emotion")
 

# path = r"C:\Users\User\Documents\adedoyin\SWEP III\model\images\img.jpg"
# print(tell_emotion(path))

# # model = load_model("emotionModel.hdf5",compile = False)
# # class FacialRecognitionViewSet(ModelViewSet):  
# #     serializer_class = EmotionSerializer
# #     queryset = Image.objects.all()

# # def shapePoints(shape):
# #     coords = np.zeros((68, 2), dtype="int")
# #     for i in range(0, 68):
# #         coords[i] = (shape.part(i).x, shape.part(i).y)
# #     return coords


# # def rectPoints(rect):
# #     x = rect.left()
# #     y = rect.top()
# #     w = rect.right() - x
# #     h = rect.bottom() - y
# #     return (x, y, w, h)

# # def tell_emotion(image):
# #     image = request.FILES.get('image')
# #     frame = imread(image)
        
# #     detector = dlib.get_frontal_face_detector()
# #     emotionTargetSize = model.input_shape[1:3]
# #     faceLandmarks = "shape_predictor_68_face_landmarks.dat"
# #     predictor = dlib.shape_predictor(faceLandmarks)

# #     grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# #     rects = detector(grayFrame, 0)
# #     if len(rects) !=0:
# #         for rect in rects:
# #             shape = predictor(grayFrame, rect)
# #             points = shapePoints(shape)
# #             (x, y, w, h) = rectPoints(rect)
# #             grayFace = grayFrame[y:y + h, x:x + w]
# #             try:
# #                 grayFace = cv2.resize(grayFace, (emotionTargetSize))
# #             except:
# #                 continue
# #             grayFace = grayFace.astype('float32')
# #             grayFace = grayFace / 255.0
# #             grayFace = (grayFace - 0.5) * 2.0
# #             grayFace = np.expand_dims(grayFace, 0)
# #             grayFace = np.expand_dims(grayFace, -1)
# #             emotion_prediction = model.predict(grayFace,verbose = 0)
# #             emotion_probability = np.max(emotion_prediction)

# #             predictions = ["Anrgy","Disgust","Fear","Happy","Sad","Suprised","neutral"]

# #             result = predictions[emotion_prediction.argmax()]
# #         else:
# #             return JsonResponse({'emotions' : result})

# #     return JsonResponse({'message': 'Invalid request method'})


# #     # path = r"C:\Users\User\Documents\adedoyin\SWEP III\model\1684844504506.jpg"
# #     # print(tell_emotion(path))