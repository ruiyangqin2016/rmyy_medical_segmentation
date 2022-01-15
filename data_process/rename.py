import os
import shutil

# Initializing variables
files_address = r"/home/ruiyang/Desktop/MSD/rmyy_segmentation/"
files = os.listdir(files_address + "rmyy/")
names = []
textfile = open("log.txt", "w")
name_reference = ''
counter = 0

# Fetch names of files except their "_image/label.nii.gz"
for f in files:
    mark = f[:-13]
    if mark not in names:
        names.append(mark)

# Clear "cache", or the files may be depublicated
if os.path.exists(files_address + "images/"): shutil.rmtree(files_address + "images/")
if os.path.exists(files_address + "labels/"): shutil.rmtree(files_address + "labels/")
os.mkdir(files_address + "images/")
os.mkdir(files_address + "labels/")
# Move images and labels to different folders
for name in names:
    # Target address
    image_dst = files_address + "images/" + name + "_image.nii.gz"
    label_dst = files_address + "labels/" + name + "_label.nii.gz"
    # Source address
    image_address = files_address + "rmyy/" + name + "_image.nii.gz"
    label_address = files_address + "rmyy/" + name + "_label.nii.gz"
    # Copy files into new folders
    shutil.copyfile(image_address, image_dst)
    shutil.copyfile(label_address, label_dst)
print("Finished files split")

# Name changing function
for name in names:
    # Setup names for name changing
    candidate = "rmyy" + str(counter) + ".nii.gz"
    old_image_name = name + "_image.nii.gz"
    old_label_name = name + "_label.nii.gz"        
    counter += 1
    # Setup addresses
    image = files_address + "images/" + name + "_image.nii.gz"
    label = files_address + "labels/" + name + "_label.nii.gz"
    new_image = files_address + "images/" + candidate
    new_label = files_address + "labels/" + candidate
    # Name Chnaging and put them into a different folder
    os.rename(image, new_image)
    os.rename(label, new_label)

    # Tracking the name changing
    node = (candidate + " -> " + name)
    textfile.write(node + "\n")
print("Finished files rename")
textfile.close()
