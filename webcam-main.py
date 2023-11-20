import cv2
import mediapipe as mp

webcam = cv2.VideoCapture(0)

# Face
face_recognition = mp.solutions.face_detection
drawing = mp.solutions.drawing_utils
face_recognizer = face_recognition.FaceDetection()

# Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()


while webcam.isOpened():
  validation, frame = webcam.read()
  if not validation:
    break
  
  imagem = frame
  list_faces = face_recognizer.process(imagem)

  if list_faces.detections:
    for rosto in list_faces.detections:
      drawing.draw_detection(imagem, rosto)

  # Hand recognition code
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