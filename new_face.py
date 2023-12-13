import face_recognition as fr
import uuid

def new_face(url_photo):
  photo = fr.load_image_file(url_photo)
  faces = fr.face_encodings(photo)
  if(len(faces) > 0):
    return True, faces
  
  return False, []

def get_faces():
  familiar_faces = []
  names_of_faces = []
  id_of_faces = []

  darlan1 = new_face("./faces/darlan.png")
  if(darlan1[0]):
    familiar_faces.append(darlan1[1][0])
    face_id = uuid.uuid4()
    id_of_faces.append(face_id)
    print({
      face_id
    })
    names_of_faces.append("Darlan")

  fernanda1 = new_face("./faces/fernanda.png")
  if(fernanda1[0]):
    familiar_faces.append(fernanda1[1][0])
    face_id = uuid.uuid4()
    id_of_faces.append(face_id)
    print({
      face_id
    })
    names_of_faces.append("Fernanda")

  ingrid1 = new_face("./faces/ingrid.png")
  if(ingrid1[0]):
    familiar_faces.append(ingrid1[1][0])
    face_id = uuid.uuid4()
    id_of_faces.append(face_id)
    print({
      face_id
    })
    names_of_faces.append("Ingrid") 

  jade1 = new_face("./faces/jade.png")
  if(jade1[0]):
    familiar_faces.append(jade1[1][0])
    face_id = uuid.uuid4()
    id_of_faces.append(face_id)
    print({
      face_id
    })
    names_of_faces.append("Jade - Dog") 

  nina1 = new_face("./faces/nina.png")
  if(nina1[0]):
    familiar_faces.append(nina1[1][0])
    face_id = uuid.uuid4()
    id_of_faces.append(face_id)
    print({
      face_id
    })
    names_of_faces.append("Nina - Dog") 

  return familiar_faces, names_of_faces, id_of_faces