import numpy as np
import cv2
import mediapipe as mp
import face_recognition as fr

from new_face import get_faces

familiar_faces, name_of_faces, id_of_faces = get_faces()

webcam = cv2.VideoCapture(0)

# Face
face_recognition = mp.solutions.face_detection
drawing = mp.solutions.drawing_utils
face_recognizer = face_recognition.FaceDetection()

# Hands 
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

def initCam():
  while webcam.isOpened():
    validation, frame = webcam.read()
    if not validation:
      break
    
    imagem = frame
    list_faces = face_recognizer.process(imagem)

    rgb_frame = np.ascontiguousarray(imagem[:, :, ::-1])

    # local_of_faces = fr.face_locations(rgb_frame)
    # unknown_faces = fr.face_encodings(rgb_frame, local_of_faces)

    if list_faces.detections:
      for rosto in list_faces.detections:

        # Different draw to recognition
        drawing.draw_detection(imagem, rosto)
        
        # There is a problem in the solution below
        # local_of_faces and unknown_faces are very slow
        # and makes the webcam slow
        # for (top, right, bottom, left), unknown_face in zip(local_of_faces, unknown_faces):
        #   results = fr.compare_faces(familiar_faces, unknown_face)

        #   face_distances = fr.face_distance(familiar_faces, unknown_face)

        #   best_match = np.argmin(face_distances)
        #   if results[best_match]:
        #     name = name_of_faces[best_match]
        #   else:
        #     name = "Desconhecido"

        #   # Around the face
        #   cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        #   # Below
        #   cv2.rectangle(frame, (left, bottom -35), (right, bottom), (0, 0, 255), cv2.FILLED)
        #   font = cv2.FONT_HERSHEY_SIMPLEX

        #   # Text
        #   cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Hand recognition code - search a usability
    rgb_frame = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
          for landmark in hand_landmarks.landmark:
              x, y = int(landmark.x * frame.shape[1]), int(landmark.y * frame.shape[0])
              cv2.circle(imagem, (x, y), 5, (0, 255, 0), -1)

    cv2.imshow("Your Webcam", imagem)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      print("The camera was closed")
      break

  webcam.release()
  cv2.destroyAllWindows()
