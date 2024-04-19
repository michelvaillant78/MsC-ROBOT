import speech_recognition as sr
import pyttsx3
import time

# Initialisation du moteur de synthèse vocale
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def write_command_to_file(command):
    with open("../data/commands.txt", "a") as file:  # "a" pour append, "w" pour écrire (efface le contenu précédent)
        file.write(command + "\n")  # Ajoute la commande au fichier avec un retour à la ligne


def read_command_from_file(filepath):
    with open("../data/commands.txt", "r") as file:
        commands = file.readlines()
    return commands


# Fonction pour écouter et reconnaître la parole
def listen():
    # Initialisation du recognizer
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)  # Ajuste dynamiquement le seuil en fonction du bruit ambiant
        print("Listening...")
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio)
            print(f"Vous avez dit: {command}")
            return command
            write_command_to_file(command)
        except Exception as e:
            print("Désolé, je n'ai pas compris. Veuillez répéter.")
            return None


# Fonction pour lire le fichier command.txt


def main():
    commands = read_command_from_file("../data/commands.txt")
    # noinspection PyTypeChecker
    for command in commands:
        command = command.strip()
        if command:
            control_robot(command.strip())
            time.sleep(1)  # Pause entre les commandes


# Fonction pour contrôler un robot
def control_robot(command):
    if command:
        if 'avance' in command:
            speak("Le robot avance")
            drive_forward()
            # Ici, ajoutez le code pour faire avancer le robot
            write_command_to_file(command)
        elif 'recule' in command:
            speak("Le robot recule")
            # Ici, ajoutez le code pour faire reculer le robot
            write_command_to_file(command)
        elif 'gauche' in command:
            speak("Le robot tourne à gauche")
            # Code pour tourner le robot à gauche
            write_command_to_file(command)
        elif 'droite' in command:
            speak("Le robot tourne à droite")
            # Code pour tourner le robot à droite
            write_command_to_file(command)
        elif 'stop' in command:
            speak("Le robot s'arrête")
            stop()
            write_command_to_file(command)
        else:
            print("Commande non reconnue")


# Boucle principale

if __name__ == "__main__":
    while True:
        command = listen()
        if command:
            control_robot(command)
