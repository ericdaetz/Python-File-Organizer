import os
import argparse

class FileOrganizer:

    types_dict = None

    #Non-listed types go into Miscellaneous Folder
    def __init__(self):
        self.types_dict = {
            "Documents": [".doc", ".docx", ".pdf", ".txt"],

            "Videos": [".wmv", ".mp4" ".mov", ".mpg", ".mpeg", ".mkv"],

            "Music": [".mp3", ".wav", ".wma", ".msv"]
        }
    

    def organizer(self):
        print(self.types_dict)
        
        

if __name__ == '__main__':
    my_organizer = FileOrganizer()
    my_organizer.organizer()