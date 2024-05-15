# Made by 0DayExploiter
# C.I.U Criminal In Uniforms 
# DISCORD:lnternetcriminal
# This Tool Is A Cleaner For Secuirity Reasons, It Cleans Cookies,
# Deleted and hidden Files
# Like CCLeaners but this can be used on Any OS 

import os
import os
import shutil

def clean_cookies(directory):
    cookie_path = os.path.join(directory, "Cookies")
    if os.path.exists(cookie_path):
        try:
            shutil.rmtree(cookie_path)
            print("Cookies cleaned successfully.")
        except Exception as e:
            print(f"Error cleaning cookies: {e}")
    else:
        print("Cookies directory not found.")

def clean_deleted_files(directory):
    deleted_files_path = os.path.join(directory, "$RECYCLE.BIN")
    if os.path.exists(deleted_files_path):
        try:
            shutil.rmtree(deleted_files_path)
            print("Deleted files cleaned successfully.")
        except Exception as e:
            print(f"Error cleaning deleted files: {e}")
    else:
        print("Deleted files directory not found.")

def clean_hidden_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.startswith('.'):  # Check if the file starts with a dot (indicating it's hidden)
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)  # Remove the hidden file
                    print(f"Deleted hidden file: {file_path}")
                except Exception as e:
                    print(f"Error deleting hidden file {file_path}: {e}")

def main():
    directory = input("Enter the directory path to clean: ")
    if os.path.exists(directory):
        clean_cookies(directory)
        clean_deleted_files(directory)
        clean_hidden_files(directory)
        print("Cleanup completed successfully.")
    else:
        print("Directory not found.")

if __name__ == "__main__":
    main()
