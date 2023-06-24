import speech_recognition as sr
import cv2
import pyttsx3
from playsound import playsound
from gtts import gTTS


webCam = cv2.VideoCapture(0)
currentframe = 0

while (True):
    success, frame = webCam.read()

    # Save Frame by Frame into disk using imwrite method
    '''cv2.imshow("Output", frame)
    cv2.imwrite(text + str(currentframe) + '.jpg', frame)
    currentframe == 1'''

    r=sr.Recognizer()
    print(sr.Microphone.list_microphone_names())
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=3)
    # r.energy_threshold()
       # print("say anything : ")
        print("Say image name:")
        def playaudio(audio):
            playsound(audio)
        def convert_to_audio(text):
            audio = gTTS(text)
            audio.save("textaudio.mp3")
            playaudio("textaudio.mp3")
        convert_to_audio("say image name")
        audio= r.listen(source)

    '''def play_audio(text):
        audio = gTTS(text)
        audio.save("textaudio.mp3")
        playsound("textaudio.mp3")

    print("Say image name:")
    play_audio("Say image name")
    audio   = r.listen(source) '''

    try:
        text = r.recognize_google(audio)
        print(text)
    except:
        print("sorry, could not recognise")

    cv2.imshow("Output", frame)
    cv2.imwrite("D:\\att\\final-attendance\\ai_vision\\images\\"+text + '.jpg',frame)
    currentframe == 1
    engine = pyttsx3.init()

# Speak the text
    engine.say(text +"image is saved")
    engine.runAndWait()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


webCam.release()


