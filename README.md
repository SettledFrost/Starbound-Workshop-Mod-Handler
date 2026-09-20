#Starbound Workshop Mod Handler

This project aims to make Starbound modded server hosting easier by automatically scanning the downloaded workshop mods from the user's computer, copying and re-naming them in a separate folder to make server mod management easier.

Ideally this tool will reduce or entirely remove the time taken hunting down workshop mods to copy for the host machine's mods folder.

How to use:

Put in your steam workshop content folder directory as ReadDir inside the config file, put the destination folder for all the sorted mods in WriteDir and your game ID as Game under "CoreIDs". Then you simply run Main.py and the script does everything for you.

WARNING!
Setting the wrong directory in the config can and most likely will lead to all of the files in the wrong directory being deleted. The script heavily relies on correct user input so make sure you are using the right directories before executing! The creator of this script is not responsible for any files lost.