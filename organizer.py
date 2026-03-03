import os
import shutil

# Path da pasta que será organizada (crie esta pasta no seu PC, na mesma pasta do script)
FOLDER_PATH = "organize_here"

# Mapeamento de extensões para pastas
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Music": [".mp3", ".wav"],
    "Videos": [".mp4", ".mkv"],
}


def get_unique_destination(folder: str, filename: str) -> str:
    """
    Gera um caminho de destino que não sobrescreve arquivo existente.
    Ex: foto.jpg -> foto_1.jpg -> foto_2.jpg ...
    """
    destination = os.path.join(folder, filename)
    name, ext = os.path.splitext(filename)

    counter = 1
    while os.path.exists(destination):
        destination = os.path.join(folder, f"{name}_{counter}{ext}")
        counter += 1

    return destination


def organize_files():
    if not os.path.exists(FOLDER_PATH):
        print("Folder does not exist.")
        return

    for file in os.listdir(FOLDER_PATH):
        file_path = os.path.join(FOLDER_PATH, file)

        # Ignora pastas
        if not os.path.isfile(file_path):
            continue

        moved = False

        # Tenta encaixar em alguma categoria
        for category, extensions in FILE_CATEGORIES.items():
            if any(file.lower().endswith(ext) for ext in extensions):
                category_path = os.path.join(FOLDER_PATH, category)
                os.makedirs(category_path, exist_ok=True)

                destination = get_unique_destination(category_path, file)
                shutil.move(file_path, destination)

                print(f"Moved: {file} → {category}/{os.path.basename(destination)}")
                moved = True
                break

        # Se não encontrou categoria, vai pra Others
        if not moved:
            others_path = os.path.join(FOLDER_PATH, "Others")
            os.makedirs(others_path, exist_ok=True)

            destination = get_unique_destination(others_path, file)
            shutil.move(file_path, destination)

            print(f"Moved: {file} → Others/{os.path.basename(destination)}")


if __name__ == "__main__":
    organize_files()
    
