import os

def fetchFolders(Directory):
    Folders = os.listdir(Directory)
    Folders = [folder for folder in Folders if os.path.isdir(os.path.join(Directory, folder))]
    return Folders

def fetchFiles(Directory):
    Files = os.listdir(Directory)
    Files = [file for file in Files if os.path.isfile(Directory+'/'+file)]
    return Files

def fetchFilesByExtension(Directory, Extension):
    FilesExt = []
    Files = fetchFiles(Directory)
    for file in Files:
        if file.endswith(Extension):
            FilesExt.append(file)
    return FilesExt