import Config as cfg
from Modules import Reader as rd

def fetchmods(Directory):
    Folders = rd.fetchFolders(Directory)
    for i, folder in enumerate(Folders):
        print(f"{i+1}. {folder}")
        if rd.fetchFiles(f"{Directory}\\{folder}"):
            for file in rd.fetchFiles(f"{Directory}\\{folder}"):
                print(f"> {file}\n")
    return

fetchmods(cfg.Directories["ReadDir"])