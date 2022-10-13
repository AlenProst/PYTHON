import glob
import os
import shutil

# Searching pattern inside folders and sub folders recursively
# search all jpg files
pattern = r"C:\Users\Ivan\Desktop\To_delete\**\.terraform"
for item in glob.iglob(pattern, recursive=True):
    # delete file
    print("Deleting:", item)
    shutil.rmtree(item)

pattern = r"C:\Users\Ivan\Desktop\To_delete\**\terraform*"
for item in glob.iglob(pattern, recursive=True):
    # delete file
    print("Deleting:", item)
    os.remove(item)

pattern = r"C:\Users\Ivan\Desktop\To_delete\**\.terraform.*"
for item in glob.iglob(pattern, recursive=True):
    # delete file
    print("Deleting:", item)
    os.remove(item)
