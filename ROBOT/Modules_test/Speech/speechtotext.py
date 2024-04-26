import speech_recognition as sr

recognizer = sr.Recognizer()

def recognize_speech(audio):
    try:
        text = recognizer.recognize_google(audio, language='fr-FR')
        return text
    except sr.UnknownValueError:
        return "Désolé, je n'ai pas compris"
    except sr.RequestError:
        return "Désolé, il y a eu une erreur de process"

def transcribe_speech():
    with sr.Microphone() as source:
        print("Je vous écoute...")
        audio = recognizer.listen(source)
    transcribed_text = recognize_speech(audio)
    if transcribed_text:
        with open("transcription.txt", "w") as file:
            file.write(transcribed_text)
        print("La transcription a été sauvegardée dans le fichier transcription.txt")
        return transcribed_text
    else:
        return "La transcription a échoué."

if __name__ == "__main__":
    transcribe_speech()
