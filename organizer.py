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
    

    def organizer(self):
        print(self.types_dict)

        curr_dir = Path('.')

        for index, entry in enumerate(curr_dir.iterdir()):
            print(f"File No:  {index}: {entry}")
        
        
if __name__ == '__main__':
    my_organizer = FileOrganizer()
    #parser = argparse.ArgumentParser()
    my_organizer.organizer()