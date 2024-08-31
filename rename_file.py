# TODO remove unwanted string pattern in filename (without changing it content)
# 100% for the present
# TODO break every task down

# TODO list filenames in current directory
import os

files = os.listdir()
for file in files:
    # assign filename
    org_filename = file
    print("filename", file)
    # TODO create new name without the unwanted pattern
    unwanted_pattern = "y2meta.com_"
    # TODO replace unwanted pattern with empty string
    new_name = org_filename.replace(unwanted_pattern, '')
    print("-> newname: ", new_name)
    # TODO rename file (which function?)

# TODO log this out, how to show command in this vs code screen (which shortcut)
# shortcut ctrl + `
    
    # TODO why it shows the .git name where did it take, is this the real folder?
