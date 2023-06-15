import tensorflow as tf
import pickle
import cv2
import numpy as np

liveness_model = tf.keras.models.load_model('liveness.model')
le = pickle.loads(open('le.pickle', 'rb').read())
detector_net = cv2.dnn.readNetFromCaffe('../model/deploy.prototxt.txt', '../model/res10_300x300_ssd_iter_140000.caffemodel')

face = cv2.imread('4.png')

# frame = imutils.resize(frame, width=800)
# (h, w) = frame.shape[:2]
# blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300,300)), 1.0, (300, 300), (104.0, 177.0, 123.0))

# detector_net.setInput(blob)
# detections = detector_net.forward()
# label_name = 'fake'

# for i in range(0, detections.shape[2]):
#     # extract the confidence (i.e. probability) associated with the prediction
#     confidence = detections[0, 0, i, 2]
    
#     print(confidence)
#     # filter out weak detections
#     if confidence > 0.5:
#         # compute the (x,y) coordinates of the bounding box
#         # for the face and extract the face ROI
#         box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
#         (startX, startY, endX, endY) = box.astype('int')
        
#         # expand the bounding box a bit
#         # (from experiment, the model works better this way)
#         # and ensure that the bounding box does not fall outside of the frame
#         startX = max(0, startX-20)
#         startY = max(0, startY-20)
#         endX = min(w, endX+20)
#         endY = min(h, endY+20)
        
        # extract the face ROI and then preprocess it
        # in the same manner as our training data

try:
    face = cv2.resize(face, (32,32))
except:
    print('ERROR')

face = face.astype('float') / 255.0 
face = tf.keras.preprocessing.image.img_to_array(face)
face = np.expand_dims(face, axis=0)
preds = liveness_model.predict(face)[0]
j = np.argmax(preds)
label_name = le.classes_[j]
print(label_name)

