import os
import re

def renameFile(Directory, OldName, NewName):

    # Characters forbidden in Windows and Linux filenames
    ForbiddenChars = r'[<>:"/\\|?*\x00]'

    # Replace forbidden characters with "-"
    NewName = re.sub(ForbiddenChars, "-", NewName)

    OldDir = os.path.join(Directory, OldName)
    NewDir = os.path.join(Directory, NewName)

    os.rename(OldDir, NewDir)