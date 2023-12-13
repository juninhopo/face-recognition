# Face Recognition with python

Performs facial and hand recognition.

## Problems to Solution

#### The webcam is very slow

- There is a problem in the solution below local_of_faces and unknown_faces are very slow and makes the webcam slow

```py
    local_of_faces = fr.face_locations(rgb_frame)
    unknown_faces = fr.face_encodings(rgb_frame, local_of_faces)
```

## Resolution to problem

Tensor flow using CPU, need install to [GPU](https://github.com/deganza/Install-TensorFlow-on-Mac-M1-GPU/blob/main/Install-TensorFlow-on-Mac-M1-GPU.ipynb)
