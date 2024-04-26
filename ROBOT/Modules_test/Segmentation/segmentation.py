import openai

def segment_text_from_file(file_path):
    # Lire le contenu du fichier
    with open(file_path, "r") as file:
        text = file.read()

    # Segmenter le texte en fonction des balises "Patient:" et "Médecin:"
    lines = text.split("\n")
    patient_text = ""
    doctor_text = ""
    patient_flag = False
    doctor_flag = False

    for line in lines:
        if "Patient:" in line:
            patient_flag = True
            doctor_flag = False
        elif "Médecin:" in line:
            patient_flag = False
            doctor_flag = True
        
        if patient_flag:
            patient_text += line + "\n"
        elif doctor_flag:
            doctor_text += line + "\n"

    return patient_text.strip(), doctor_text.strip()


def main():
    # Chemin du fichier transcription.txt
    file_path = "transcription.txt"

    # Segmenter le texte extrait du fichier
    patient_text, doctor_text = segment_text_from_file(file_path)

    # Afficher les textes segmentés
    print("Texte du patient:")
    print(patient_text)
    print("\nTexte du médecin:")
    print(doctor_text)

    # Ajoutez ici le code pour résumer les textes du patient et du médecin
    # et exécuter les commandes en fonction des requêtes du médecin

if __name__ == "__main__":
    main()


