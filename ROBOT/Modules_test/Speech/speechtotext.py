import os
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

def transcribe_audio(file_path):
    with sr.AudioFile(file_path) as source:
        audio = recognizer.record(source)
    transcribed_text = recognize_speech(audio)
    if transcribed_text:
        with open("transcription.txt", "w") as file:
            file.write(transcribed_text)
        print("La transcription a été sauvegardée dans le fichier transcription.txt")
        return transcribed_text
    else:
        return "La transcription a échoué."

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
    print("Voulez-vous enregistrer un audio depuis un microphone (M) ou transcrire un fichier audio (A) ?")
    choice = input("Entrez 'M' pour microphone ou 'A' pour fichier audio : ")

    if choice.lower() == 'm':
        transcribe_speech()
    elif choice.lower() == 'a':
        file_path = input("Entrez le chemin du fichier audio : ")
        transcribe_audio(file_path)
    else:
        print("Choix invalide. Veuillez entrer 'M' pour microphone ou 'A' pour fichier audio.")

def load_intent_mapping(file_path):
    intent_mapping = {}
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for i in range(0, len(lines), 2):
            intent = lines[i].strip().split(': ')[1]
            command = lines[i+1].strip().split(': ')[1]
            intent_mapping[intent] = command
    return intent_mapping

def process_intent(transcribed_text, intent_mapping):
    # Conversion du texte transcrit en minuscules pour une correspondance insensible à la casse
    transcribed_text = transcribed_text.lower()

    # Vérifie si l'intention est dans le dictionnaire
    for intent, command in intent_mapping.items():
        if intent in transcribed_text:
            return command
    
    return "Commande non reconnue"

if __name__ == "__main__":
    # Chemin du fichier intent_mapping.txt
    module_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(module_dir, "../Speech/intent_mapping.txt")

    # Charger le mapping des intentions et des commandes depuis un fichier
    intent_mapping = load_intent_mapping(file_path)

    # Exemple d'utilisation
    transcribed_text = "Je veux que le robot avance"
    print(process_intent(transcribed_text, intent_mapping))