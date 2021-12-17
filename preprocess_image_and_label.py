import SimpleITK as sitk
import numpy as np
import os
import matplotlib.pyplot as plt

folder_address = r"/home/ruiyang/Desktop/nnunet/nnUNet_raw/nnUNet_raw_data/Task11_rmyy/"
labels = os.listdir(folder_address + "labelsTr/")
for label_name in labels:
    label_address = folder_address + "labelsTr/" + label_name
    label = sitk.ReadImage(label_address)
    label.SetOrigin((0, 0, 0))
    sitk.WriteImage(label, label_address)
    print("Finish ", label_name)

# img = sitk.ReadImage("/home/ruiyang/Desktop/nnunet/nnUNet_raw/nnUNet_raw_data/Task11_rmyy/labelsTr/rmyy0.nii.gz")
# img.SetOrigin((0, 0, 0))
# sitk.WriteImage(img, "/home/ruiyang/Desktop/nnunet/nnUNet_raw/nnUNet_raw_data/Task11_rmyy/labelsTr/rmyy0.nii.gz")
# print (img.GetOrigin())