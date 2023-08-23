import os, sys

folders = os.listdir(os.getcwd())
for folder in folders:
    if os.path.isdir(folder):
        # rename if dirname has 6 digits
        if len(folder) == 6 and folder.isnumeric():
            day = folder[0:2]
            month = folder[2:4]
            year = folder[4:6]
            new_name = f'{year}{month}{day}'
            print(f'renaming {folder} to {new_name}')
            os.rename(folder, new_name)