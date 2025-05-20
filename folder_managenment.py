import os

def clear_folder(folder_path):
    if os.path.exists(folder_path):
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)

def folder_existence(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    