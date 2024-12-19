import os
import shutil
import time
import gzip
import fnmatch
import pickle
import hashlib
import tkinter as tk
import matplotlib.pyplot as plt
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from tkvideo import tkvideo
from PIL import Image

undo_stack = []

# CHOICE ONE: File Operations

def copyFile(fName: str, nDir: str) -> None:
    try:
        shutil.copy(fName, nDir)
        print(f"{fName} has been copied to {nDir}.")
    except Exception as e:
        print(f"Error copying file: {e}")

def deleteFile(fName: str, fPath: str) -> None:
    try:
        path: str = os.path.join(fPath, fName)
        os.remove(path)
        undo_stack.append(("delete", path))
        print(f"{fName} has been deleted.")
    except Exception as e:
        print(f"Error deleting file: {e}")

def renameFile(fName: str, nName: str) -> None:
    try:
        os.rename(fName, nName)
        undo_stack.append(("rename", nName, fName))
        print(f"{fName} has been named {nName}.")
    except Exception as e:
        print(f"Error renaming file: {e}")

def compressFile(fName: str) -> None:
    try:
        newFile: str = fName.split('.')[0] + '.gz'
        with open(fName, 'rb') as iFile:
            with gzip.open(newFile, 'wb') as oFile:
                shutil.copyfileobj(iFile, oFile)
        print(f"Created {newFile} successfully.")
    except Exception as e:
        print(f"Error compressing file: {e}")

def fileOpr() -> None:
    print("1: Copy file to another directory")
    print("2: Delete file")
    print("3: Rename file")
    print("4: Compress file")
    while True:
        ch = int(input("Choose a function: "))
        if ch == 1:
            fileName: str = input("Enter file name to be copied: ")
            newDirectory: str = input("Enter file directory to be pasted: ")
            copyFile(fileName, newDirectory)
        elif ch == 2:
            fileName: str = input("Enter file name to be deleted: ")
            filePath: str = input("Enter file path: ")
            deleteFile(fileName, filePath)
        elif ch == 3:
            fileName: str = input("Enter file name to be renamed: ")
            newName: str = input("Enter new file name: ")
            renameFile(fileName, newName)
        elif ch == 4:
            fileName: str = input("Enter file name to be compressed: ")
            compressFile(fileName)
        else:
            print("Enter a valid choice")

# CHOICE TWO: Search and Filter

def searchAndFilter() -> None:
    dire: str = input("Enter file directory: ")
    pat: str = "*" + input("Enter file extension: ")
    ch: str = input("Would you like to enter date (y/n): ")
    matches: list[str] = []
    if ch == 'y':
        date = input("Enter date of creation: ")
    with os.scandir(dire) as files:
        for file in files:
            if fnmatch.fnmatch(file.name, pat) and file.is_file():
                if ch == 'y':
                    file_date = time.strftime('%Y-%m-%d', time.localtime(file.stat().st_mtime))
                    if date == file_date:
                        matches.append(file.path)
                else:
                    matches.append(file.path)
    print(matches)

# CHOICE THREE: File Preview

def filePreview() -> None:
    fileName: str = input("Enter file name: ")
    ext: str = fileName.split('.')[-1].lower()
    if ext == 'txt':
        with open(fileName, 'r') as file:
            data: str = file.read()
        print(data)
    elif ext == 'dat':
        with open(fileName, 'rb') as file:
            data: str = pickle.load(file)
        print(data)
    elif ext == 'png' or ext == 'jpg':
        img = Image.open(fileName)
        img.show()
    elif ext == "mp4":
        window = tk.Tk()
        window.title("Tkinter Video Player")
        window.geometry("800x600")

        video_label = tk.Label(window)
        video_label.pack(expand=True, fill="both")

        player = tkvideo(fileName, video_label, loop=1)
        player.play()

        window.mainloop()
    else:
        print("Enter a readable file.")

# CHOICE FOUR: Duplicate File Finder

def hash_file(file_path: str) -> str:
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def dup() -> None:
    directory: str = input("Directory to be searched: ")
    filehashes: dict = {}

    for root, dirs, files in os.walk(directory):
        for file in files:
            filePath = os.path.join(root, file)
            filehash = hash_file(filePath)
            if filehash in filehashes:
                print(f"Found duplicate file {filePath} in {directory}.")
                os.remove(filePath)
                print("File has been deleted.")
            else:
                filehashes[filehash] = filePath

    print("Finished searching for duplicates.")

# CHOICE FIVE: Temporary Storage

def tempStorage() -> None:
    try:
        fileName: str = input("Enter file name: ")
        recycleBin = os.path.join(os.path.expanduser("~"), ".recycleBin")
        os.makedirs(recycleBin, exist_ok=True)
        shutil.move(fileName, recycleBin)
        undo_stack.append(("restore", os.path.join(recycleBin, fileName), fileName))
        print(f"{fileName} has been temporarily stored in the recycleBin.")
    except Exception as e:
        print(f"Error moving file to recycleBin: {e}")

# CHOICE SIX: Cloud Integration
def cloud() -> None:
    try:
        fileName: str = input("Enter file name: ")

        if not os.path.isfile(fileName):
            print(f"File {fileName} does not exist.")
            return

        gauth = GoogleAuth()
        gauth.LocalWebserverAuth()
        drive = GoogleDrive(gauth)

        file = drive.CreateFile({'title': os.path.basename(fileName)})
        file.SetContentFile(fileName)
        file.Upload()

        print(f"File {fileName} uploaded successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# CHOICE SEVEN: Disk Usage Statistics

def calculate_size(directory: str) -> int:
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

def diskStats() -> None:
    try:
        directory: str = input("Enter directory: ")
        dir_sizes = {}

        for dirpath, dirnames, filenames in os.walk(directory):
            for dirname in dirnames:
                subdir_path = os.path.join(dirpath, dirname)
                dir_sizes[subdir_path] = calculate_size(subdir_path)

        sorted_dir_sizes = sorted(dir_sizes.items(), key=lambda item: item[1], reverse=True)

        top_dirs = sorted_dir_sizes[:9]
        others_size = sum(size for _, size in sorted_dir_sizes[10:])

        labels = [os.path.basename(item[0]) for item in top_dirs]
        sizes = [item[1] for item in top_dirs]

        if others_size > 0:
            labels.append("Others")
            sizes.append(others_size)

        plt.figure(figsize=(10, 6))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title('File Sizes')
        plt.axis('equal')  
        plt.show()
        
    except FileNotFoundError:
        print(f"Directory {directory} cannot be read.")

# CHOICE EIGHT: Undo

def Undo() -> None:
    if not undo_stack:
        print("No actions to undo.")
        return
    action = undo_stack.pop()
    try:
        if action[0] == "delete":
            print(f"Cannot undo delete: {action[1]}")
        elif action[0] == "restore":
            shutil.move(action[1], action[2])
            print(f"Restored file to {action[2]}")
        elif action[0] == "rename":
            os.rename(action[1], action[2])
            print(f"File renamed back to {action[2]}")
    except Exception as e:
        print(f"Error during undo: {e}")

def main():
    print("-------File Manager-------")
    print("1: File Operations")
    print("2: Search and Filter")
    print("3: File Preview")
    print("4: Duplicate File Finder")
    print("5: Temporary Storage")
    print("6: Cloud Integration")
    print("7: Disk Usage Statistics")
    print("8: Undo")
    print("9: Exit")

    cont = "yes"  
    while cont == "yes":
        try:
            choice = int(input("Enter a valid choice: "))
            if choice == 1:
                fileOpr()
            elif choice == 2:
                searchAndFilter()
            elif choice == 3:
                filePreview()
            elif choice == 4:
                dup()
            elif choice == 5:
                tempStorage()
            elif choice == 6:
                cloud()
            elif choice == 7:
                diskStats()
            elif choice == 8:
                Undo()
            elif choice == 9:
                print("Exiting Program.....")
                time.sleep(5)
                print("Thanks for visiting")
                break
            else:
                print("Enter a valid choice (1-9).")
            cont = input("Would you like to continue (yes/no): ").lower()
        except ValueError:
            print("Please enter a valid number (1-9).")
       
if __name__=="__main__":
    main()
