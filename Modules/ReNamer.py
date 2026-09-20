import os

def renameFile(Directory, OldName, NewName):
    OldDir = os.path.join(Directory, OldName)
    NewDir = os.path.join(Directory, NewName)
    os.rename(OldDir, NewDir)