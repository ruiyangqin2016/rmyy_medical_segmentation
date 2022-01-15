import SimpleITK as sitk
import os
import shutil

# Initializing variables
files_address = r"/home/ruiyang/Desktop/MSD/rmyy_segmentation/"
images_address = files_address + "images/"
labels_address = files_address + "labels/"
images = os.listdir(images_address)
labels = os.listdir(labels_address)

# Clear "cache"
if os.path.exists(files_address + "imagesTr/"): shutil.rmtree(files_address + "imagesTr/")
if os.path.exists(files_address + "labelsTr/"): shutil.rmtree(files_address + "labelsTr/")
os.mkdir(files_address + "imagesTr/")
os.mkdir(files_address + "labelsTr/")

# # Reprocess labels
# for label in labels:
#     itk_img = sitk.ReadImage(images_address + label)
#     img = sitk.GetArrayFromImage(itk_img)
#     out = sitk.GetImageFromArray(img)
#     sitk.WriteImage(out, files_address + "labelsTr/" + label)

# Reprocess images
for image in images:
    itk_img = sitk.ReadImage(images_address + image)
    img = sitk.GetArrayFromImage(itk_img)
    out = sitk.GetImageFromArray(img)
    sitk.WriteImage(out, files_address + "imagesTr/" + image)



# itk_img = sitk.ReadImage('./rmyy0.nii.gz')
# img = sitk.GetArrayFromImage(itk_img)

# out = sitk.GetImageFromArray(img)
# sitk.WriteImage(out, 'rmyy0_conv.nii.gz')
