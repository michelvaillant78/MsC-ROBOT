import os

def load_intent_mapping(file_path):
    intent_mapping = {}
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for i in range(0, len(lines), 2):
                intent = lines[i].strip().split(': ')[1]
                command = lines[i+1].strip().split(': ')[1]
                intent_mapping[intent] = command
    except IndexError:
        print("Erreur : Format de fichier incorrect. Assurez-vous que chaque intention est suivie de sa commande.")
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
    # Charger le mapping des intentions et des commandes depuis un fichier
    module_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(module_dir, "../Speech/intent_mapping.txt")
    intent_mapping = load_intent_mapping(file_path)

    # Vérification du mapping chargé
    if intent_mapping:
        print("Mapping des intentions et des commandes :")
        for intent, command in intent_mapping.items():
            print(f"{intent} : {command}")

        # Transcription texte
        transcribed_text = "Je veux que le robot avance"  # Remplacez ceci par la transcription réelle

        # Processus d'intention
        command = process_intent(transcribed_text, intent_mapping)
        if command != "Commande non reconnue":
            print(f"L'intention est : {transcribed_text}")
            print(f"Commande à exécuter : {command}")
            # Ici, vous pouvez ajouter le code pour exécuter la commande
        else:
            print("Commande non reconnue")
    else:
        print("Erreur : Impossible de charger le mapping des intentions et des commandes.")