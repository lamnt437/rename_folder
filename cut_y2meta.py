import os

items = os.listdir()
removed_strings = ["y2meta.com - "]
for item in items:
    print("item", item)
    if not item.endswith('.mp3'):
        continue
    for removed_string in removed_strings:
        if removed_string in item:
            new_name = item
            new_name = new_name.replace(removed_string, '')
            print("new_name", new_name)
            os.rename(item, new_name)