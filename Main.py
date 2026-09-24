import Config as cfg
import os
from time import sleep as wait
from time import sleep as wait

from Modules import Purge as p

from Modules import Reader as rd
from Modules import Workshop as ws
from Modules import Cloner as cl
from Modules import ReNamer as rn

from Modules import Loading as ld

#Do not touch this, this defines what the read directory actually is, combines steam workshop directory with the game ID.
Read = f"{cfg.Directories["SteamDir"]}\\{cfg.CoreIDs["Game"]}"

#Do not touch this, this defines what the write directory actually is.
Write = f"{cfg.Directories["WriteDir"]}"

#Do not touch this, this defines what the expected file within each folder will be named, you can tweak this in Config.py
DefaultFile = f"{cfg.ModInfo["ExpectedName"]}{cfg.ModInfo["ExpectedExt"]}"

#Function to clear console screen
def clr():
    os.system("cls")

#Function to count the "mods" in a specified directory
def countMods(Directory):
    Folders = rd.fetchFolders(Directory)
    return len(Folders)

#Function to reset the screen, mimic screen refreshing
def resetScreen(Purged):
    clr()
    if Purged >= 1:
        print(f"{Purged} files were detected and deleted.\n")
    elif Purged <= -1:
        pass
    else:
        print("No files were detected for deletion.\n")
    return

#Function to check if the read and write directories exist
def PreFlight():
    if not os.path.exists(Read):
        exit
    elif not os.path.exists(Write):
        exit
    pass

#Function to find and delete any and all contents of the clone target directory
def Step1():
    #Clear the command line with purged files set as 0
    resetScreen(-1)
    #Print message
    print("Scanning for files in target directory...")
    wait(3)
    #Set the counter of the deleted files as the number of files getting deleted
    Deleted = p.purgeDir(Write)
    #Wait a second before resetting the screen.
    wait(1)
    #Reset the screen again with the purged file info updated.
    resetScreen(Deleted)

#Function to get the names of all mods in the read directory
def Step2(List):
    #Blank dictionary to start
    result = {}
    #For each mod
    for i, mod in enumerate(List):
        #Placeholder name
        name = "Not_Found"
        #Set the name as the result of a workshop search
        name = ws.fetchWorkshopName(mod)
        #Add the mod info to the dictionary
        result.update({mod: name})
        #Print the loading info
        ld.printLoadBar(i+1, len(List), "Naming")
    resetScreen(0)
    return result

#Function to clone files into target write directory
def Step3(Dictionary):
    #Get a list of all keys or mod IDs
    keys = Dictionary.keys()
    #For each key
    for i, key in enumerate(keys):
        #Clone the mod into the write directory
        cl.cloneFile(f"{Read}\\{key}", DefaultFile, Write)
        #Rename the mod
        rn.renameFile(Write, DefaultFile, Dictionary[f"{key}"])
        #Update the load bar
        ld.printLoadBar(i+1, len(keys), "Clone")

if __name__ == "__main__":
    #Check if the read and write directories exist
    PreFlight()
    #Delete anything in the write directory
    Step1()
    #Get a list of all the mod IDs
    modList = rd.fetchFolders(Read)
    #Use the list of mod IDs to get names
    Names = Step2(modList)
    #Copy and re-name mods into target folder
    Step3(Names)