import cv2
import pickle
from playsound import playsound
from gtts import gTTS
import numpy as np
import face_recognition
import os
import pyttsx3




path = 'D:\\att\\final-attendance\\ai_vision\\images' #change to the path where images are stored
images = []
personNames = []
myList = os.listdir(path)
print(myList)
for cu_img in myList:
    current_Img = cv2.imread(f'{path}/{cu_img}')
    images.append(current_Img)
    personNames.append(os.path.splitext(cu_img)[0])
print(personNames)

#with open("names.pickle", "wb") as f:
#   pickle.dump(personNames, f) 


def faceEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encodings = face_recognition.face_encodings(img)
        if len(encodings) > 0:
            encode = encodings[0]
            encodeList.append(encode)
    return encodeList

encodeListKnown = faceEncodings(images)
print('All Encodings Completed!!!')

'''def playaudio(audio):
    playsound(audio)
def convert_to_audio(text):
    audio = gTTS(text)
    audio.save("identify.mp3")
    playaudio("identify.mp3")
convert_to_audio("All Encodings Completed")
'''





cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    faces = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
    faces = cv2.cvtColor(faces, cv2.COLOR_BGR2RGB)

    facesCurrentFrame = face_recognition.face_locations(faces)
    encodesCurrentFrame = face_recognition.face_encodings(faces, facesCurrentFrame)

    for encodeFace, faceLoc in zip(encodesCurrentFrame, facesCurrentFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        matchIndex = np.argmin(faceDis)
        
        if matches[matchIndex]:
            name = personNames[matchIndex].upper()

            def playaudio(audio):
                playsound(audio)
            def convert_to_audio(text):
                audio = gTTS(text)
                audio.save("speak.mp3")
                playaudio("speak.mp3")
            convert_to_audio("hello "+name)
        else:
            import image_storage
    cv2.imshow('Webcam', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
