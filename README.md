# Face Recognition with python

Performs facial and hand recognition.

## Problems to Solution

#### The webcam is very slow

- There is a problem in the solution below local_of_faces and unknown_faces are very slow and makes the webcam slow

```py
    local_of_faces = fr.face_locations(rgb_frame)
    unknown_faces = fr.face_encodings(rgb_frame, local_of_faces)
```
