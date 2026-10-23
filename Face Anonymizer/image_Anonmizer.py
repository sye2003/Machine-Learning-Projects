import cv2
import mediapipe as mp


def face_detection_img(img,face_detections):
     img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
     out = face_detection.process(img_rgb)

   # print(out.detections)

     if out.detections is not None:
      for detection in out.detections:
        location_data = detection.location_data
        bbox = location_data.relative_bounding_box

        x1,y1,w,h = bbox.xmin,bbox.ymin, bbox.width, bbox.height
        x1 = int(x1 *W)
        y1 = int(y1 *H)
        w = int(w *W)
        h = int(h *H)

        #image=cv2.rectangle(image,(x1,y1),(x1+w,y1+h),(0,255,0),5)
        #blur image
        img[y1:y1+h,x1:x1 + w, :]= cv2.blur(image[y1:y1+h,x1:x1 + w, :],(30,30))

     
     return img   


image_orginal= cv2.imread("faceimage.jpg")

image=cv2.resize(image_orginal, (640, 480))#cv2.resize(image_orginal,(0,0),fx=0.5,fy=0.5)


H, W,C =image.shape

#if image is None:
   # print("Failed to load image. Check the filename and extension.")
#else:
    
    #cv2.imshow("Image", image)
   # cv2.waitKey(0)  
    #cv2.destroyAllWindows()

mp_face_detection = mp.solutions.face_detection

with mp_face_detection.FaceDetection(model_selection=0,min_detection_confidence=0.5) as face_detection:
  image= face_detection_img(image,face_detection)

cv2.imshow('image',image)
cv2.waitKey(0)

   

#  Save the image
#cv2.imwrite("anonymized_face.jpg", image)

cv2.destroyAllWindows()