import os
import shutil
from Modules import Loading
from time import sleep as wait

#Function to purge a specified directory
def purgeDir(Directory):
    #Count how many files were deleted
    count = 0
    #Get a list of all items within the directory
    contents = os.listdir(Directory)
    #Get the count of all items within the directory
    items = len(contents)
    #For every file
    for file in contents:
        #Get the file directory
        item = os.path.join(Directory, file)

        #Placeholder Var
        isFile = None

        #If the file exists then
        if os.path.exists(item):
            #If the file is a file
            if os.path.isfile(item):
                #Change the placeholder
                isFile = True
                #Delete the file
                os.remove(item)
                #Add 1 to the count
                count+=1
            #Otherwise it's a folder
            elif os.path.isdir(item):
                #Change the placeholder
                isFile = False
                #Delete the folder
                shutil.rmtree(item)
                #Add 1 to the count
                count+=1
        Loading.printLoadBar(count, items, "Del")
        #If placeholder is true, print that a file was removed
        if isFile == True:
            print(f"Item deleted: [File] | {file}")
        #If placeholder is false, print that a folder was removed
        elif isFile == False:
            print(f"Item deleted: [Folder] | {file}")
        wait(0.25)
    #Pretty self explanatory
    return count