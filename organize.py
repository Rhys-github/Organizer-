import os
import shutil

from_dir = "C:/Users/hp/Desktop"     
to_dir = "C:/Users/hp/Desktop"

list_of_files = os.listdir(from_dir)
#print(list_of_files)

#Move all "Image files" from Downloads folder to another folder
for file_name in list_of_files:
    name,extension = os.path.splitext(file_name)
    #print(name)
    #print(extension)
    #print("*****")
    if extension == " ":
        continue

    if extension in [".pdf"]:
        path1 = from_dir + "/" + file_name
        path2 = to_dir + "/" + "RhysPdf"
        path3 = to_dir + "/" + "RhysPdf" + "/" + file_name

        #print("path1: ", path1)
        #print("path3: ", path3)
        #print("****")

        #Check if Folder/Directory path exists before moving
        #Else make a new folder/directory then move
        if os.path.exists(path2) : 
            print("Moving " + file_name + "....")

            #moving from path1 to path3
            shutil.move(path1 , path3)
        else : 
            os.makedirs(path2)
            print("Moving " + file_name + "....")

            #moving from path1 to path3
            shutil.move(path1 , path3)
