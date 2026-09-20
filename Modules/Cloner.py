import shutil
import os

def cloneFile(SourceDirectory, FileName, DestinationDirectory):

    Source = os.path.join(SourceDirectory, FileName)
    Destination = os.path.join(DestinationDirectory, FileName)

    shutil.copy2(Source, Destination)