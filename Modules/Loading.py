import os

def printLoadBar(current, maximum, mode):

    process = "Error"

    if mode == "Del":
        process = "Deleted"
    elif mode == "Naming":
        process = "Named"

    #Get the percentage for the bar
    percentage = current / maximum
    #Bar Length
    length = 30
    #Set how much of the bar is filled out
    filled = int(length * percentage)
    #Set the bar
    bar = "█" * filled + "-" * (length - filled)
    #Print the bar
    os.system("cls")
    print(f"\r[{bar}] {current}/{maximum} {process}\n\n", end="")