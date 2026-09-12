import os

from Config import Directories

ReadDir = Directories["ReadDir"]

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

print(fetchFilesByExtension(ReadDir, ".txt"))