import os
import shutil

# Path da pasta que será organizada
FOLDER_PATH = "organize_here"

# Mapeamento de extensões para pastas
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Music": [".mp3", ".wav"],
    "Videos": [".mp4", ".mkv"],
}


def organize_files():
    if not os.path.exists(FOLDER_PATH):
        print("Folder does not exist.")
        return

    for file in os.listdir(FOLDER_PATH):
        file_path = os.path.join(FOLDER_PATH, file)

        if os.path.isfile(file_path):
            for category, extensions in FILE_CATEGORIES.items():
                if any(file.lower().endswith(ext) for ext in extensions):
                    category_path = os.path.join(FOLDER_PATH, category)

                    if not os.path.exists(category_path):
                        os.makedirs(category_path)

                    shutil.move(file_path, os.path.join(category_path, file))
                    print(f"Moved: {file} → {category}/")
                    break


if __name__ == "__main__":
    organize_files()
