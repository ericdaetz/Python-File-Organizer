import os
import shutil
from pathlib import Path
import argparse

class FileOrganizer:

    types_dict = None

    def __init__(self):
        self.types_dict = {
            "Documents": [".doc", ".docx", ".pdf", ".txt"],

            "Images": [".jpeg", ".jpg", ".png", ".svg", ".gif"],

            "Videos": [".wmv", ".mp4" ".mov", ".mpg", ".mpeg", ".mkv"],

            "Music": [".mp3", ".wav", ".wma", ".msv"]
        }

        self.safety_off = False
    
    #Only organizes current directory, avoids user unfamiliarity with file paths
    def organizer(self, safety_var):

        curr_dir = Path('.')

        for index, entry in enumerate(curr_dir.iterdir()):
           #DEBUG ONLY: print(f"File No:  {index + 1}: {entry.name}. Is_Dir: {entry.is_dir()}")
        
            try:
                
                if(entry.is_dir()):
                    continue

                extension_arr = entry.name.split(".") if \
                                "." in entry.name else None

                if extension_arr == None:
                    print(f"Could not determine file type for {entry.name}. Skipping file.")
                    continue

                extracted_type = "." + extension_arr[-1]

                selected_folder = None
                
                for key in self.types_dict.keys():
                    if extracted_type in self.types_dict.get(key):
                        selected_folder = str(key)
                        break
                
                if selected_folder == None:
                    print(f"Unsupported file type for {entry.name}")
                else:
                    checked_path = selected_folder + "/" + entry.name
                    if Path(checked_path).exists():
                        print(f"WARNING: \"{checked_path}\" already exists in folder \"{selected_folder}\". " 
                        f"Would you like to overwrite the existing file?"
                         "\nY/N")
                        answer_flag = False
                        while(not answer_flag):
                            answer = input()
                            answer = str.lower(answer)
                            if answer in ["yes", "y"]:
                                answer_flag = True
                                print("Confirmed. Replacing file.")
                                Path(entry.name).replace(checked_path)
                            elif answer in ["no", "n"]:
                                answer_flag = True
                                print("File replacement aborted.")
                            else:
                                print("Could not parse answer. Please answer Y/N.")

                    else:
                        if not Path(selected_folder).exists():
                            Path(selected_folder).mkdir()

                        Path(entry.name).replace(checked_path)
                    
                #DEBUG ONLY: print(extracted_type)

                
           
            except Exception as e:
                print(f"An exception occurred while parsing file {entry.name}. Could not complete organization of files. Program terminating.")
                print(e)
                return
        
        return
        
        
if __name__ == '__main__':
    my_organizer = FileOrganizer()
    #parser = argparse.ArgumentParser()
    print("This is a simple file organizer program. Please use the -h flag for more information.\n")
    my_organizer.organizer(False)