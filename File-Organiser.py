import os
import shutil

# Benutzerabfragen
input_Dokumente = input("In Dokument-Ordner sortieren? (ja/nein): ").lower() == "ja"
input_Bilder = input("In Bilder-Ordner sortieren? (ja/nein): ").lower() == "ja"
input_Archive = input("In Archiv-Ordner sortieren? (ja/nein): ").lower() == "ja"
input_Präsentationen = input("In Präsentations-Ordner sortieren? (ja/nein): ").lower() == "ja"

def main():
    file_types = {
        "Bilder": [".jpg", ".png", ".webp", ".jpeg", ".bmp", ".psd", ".avif", ".gif"],
        "Dokumente": [".pdf", ".odt", ".doc", ".docx", ".txt", ".rtf"],
        "Archive": [".tar", ".7z", ".zip", ".rar", ".tar.gz"],
        "Präsentationen": [".odp", ".ppt", ".pptx"],
        "Filme": [".mov", ".mp4", ".mkv"],
        "Audio": [".mp3", ".aac", ".wav", ".flac", ".ogg"],
    }

    # Nur die gewählten Kategorien
    selected_categories = []
    if input_Dokumente:
        selected_categories.append("Dokumente")
    if input_Bilder:
        selected_categories.append("Bilder")
    if input_Archive:
        selected_categories.append("Archive")
    if input_Präsentationen:
        selected_categories.append("Präsentationen")

    file_root = "./"  # aktuelles Verzeichnis

    def Ordner_erstellen(base_dir, folders):
        for folder in folders:
            folder_path = os.path.join(base_dir, folder)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

    def Dateien_sortieren(base_dir, types_dict, selected):
        for file in os.listdir(base_dir):
            file_path = os.path.join(base_dir, file)
            if os.path.isfile(file_path):
                _, ext = os.path.splitext(file)
                for category in selected:
                    if ext.lower() in types_dict[category]:
                        zielordner = os.path.join(base_dir, category)
                        shutil.move(file_path, os.path.join(zielordner, file))
                        print(f"Verschoben: {file} -> {category}")
                        break

    Ordner_erstellen(file_root, selected_categories)
    Dateien_sortieren(file_root, file_types, selected_categories)

if __name__ == "__main__":
    main()
        
        
    
    
    
 



