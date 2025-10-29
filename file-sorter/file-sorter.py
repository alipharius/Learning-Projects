import os
import shutil

def create_folder(path : str, extention : str):
    folder_name = extention[1:]
    folder_path = os.path.join(path, folder_name)
    os.makedirs(folder_path, exist_ok = True)
    return folder_path

def sort_file(source_path : str):
    for root_dir, sub_dirs, filenames in os.walk(source_path):
        for filename in filenames:
            file_path = os.path.join(root_dir, filename)
            extention = os.path.splitext(filename)[1]
            if extention:
                target_folder =create_folder(source_path, extention)
                target_folder = os.path.join(target_folder, filename)
                shutil.move(file_path,target_folder)

def remove_empty_folders(path: str):
    for root_dir, sub_dirs, _ in os.walk(path, topdown=False):
        for dir_name in sub_dirs:
            dir_path = os.path.join(root_dir, dir_name)
            if not os.listdir(dir_path):
                os.rmdir(dir_path)

def main():
    source_path = input("Enter the path to the source directory: ")
    sort_file(source_path)
    remove_empty_folders(source_path)
    print("Sorting complete.")

if __name__ == "__main__":
    main()                


