import sys
import os

# Ajoutez le répertoire Speech au chemin de recherche des modules pour pouvoir importer speechtotext
sys.path.append(os.path.join(os.path.dirname(__file__), '../Speech'))

from speechtotext import recognize_speech, process_intent

if __name__ == "__main__":
    # Chemin du fichier intent_mapping.txt
    module_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(module_dir, "../Speech/intent_mapping.txt")

    # Charger le mapping des intentions et des commandes depuis un fichier
    intent_mapping = process_intent.load_intent_mapping(file_path)

    # Exemple d'utilisation
    transcribed_text = "Je veux que le robot avance"
    transcribed_text = recognize_speech(transcribed_text)
    command = process_intent(transcribed_text, intent_mapping)
    print(f"Commande associée : {command}")
