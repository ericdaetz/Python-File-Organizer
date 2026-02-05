import os
from pathlib import Path
#import argparse

class FileOrganizer:

    types_dict = None

    def __init__(self):
        self.types_dict = {
            "Documents": [".doc", ".docx", ".pdf", ".txt"],

            "Images": [".jpeg", ".jpg", ".png", ".svg", ".gif"],

            "Videos": [".wmv", ".mp4" ".mov", ".mpg", ".mpeg", ".mkv"],

            "Music": [".mp3", ".wav", ".wma", ".msv"]
        }
    
    #Only organizes current directory, avoids user unfamiliarity with file paths
    def organizer(self):

        curr_dir = Path('.')

        for index, entry in enumerate(curr_dir.iterdir()):
           #DEBUG ONLY: print(f"File No:  {index + 1}: {entry.name}. Is_Dir: {entry.is_dir()}")
        
            try:
                extension = entry.name    
           
            except:
                print("An exception occurred while parsing file {entry.name}. Could not complete organization of files.")
                return
        
        return
        
        
if __name__ == '__main__':
    my_organizer = FileOrganizer()
    #parser = argparse.ArgumentParser()
    my_organizer.organizer()