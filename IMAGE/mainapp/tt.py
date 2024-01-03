import dlib
import cv2
import numpy as np
from keras.models import load_model
from matplotlib.image import imread

 
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

def get_emotion(image_path):
    frame = imread(image_path)

    detector = dlib.get_frontal_face_detector()
    emotionTargetSize = model.input_shape[1:3]
    faceLandmarks = "shape_predictor_68_face_landmarks.dat"
    predictor = dlib.shape_predictor(faceLandmarks)
     
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rects = detector(grayFrame, 0)
    for rect in rects:
        shape = predictor(grayFrame, rect)
        points = shapePoints(shape)
        (x, y, w, h) = rectPoints(rect)
        grayFace = grayFrame[y:y + h, x:x + w]
        try:
            grayFace = cv2.resize(grayFace, (emotionTargetSize))
        except:
            continue
        grayFace = grayFace.astype('float32')
        grayFace = grayFace / 255.0
        grayFace = (grayFace - 0.5) * 2.0
        grayFace = np.expand_dims(grayFace, 0)
        grayFace = np.expand_dims(grayFace, -1)
        emotion_prediction = model.predict(grayFace,verbose = 0)
        emotion_probability = np.max(emotion_prediction)

        predictions = ["Anrgy","Disgust","Fear","Happy","Sad","Suprised","neutral"]
        result = predictions[emotion_prediction.argmax()]

    return result


path = r"C:\Users\User\Documents\adedoyin\SWEP III\IMAGE\media\media\images\img.jpg"
emotion = get_emotion(path)
print(emotion)

