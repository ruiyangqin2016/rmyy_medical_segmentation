

# 2D U-Net
for f in 0 1 2 3 4
do
    printf "====================2D U-Net: fold $f===================="
    nnUNet_train 2d nnUNetTrainerV2 Task011_rmyy $f --npz
done

# 3D full resolution U-Net
for f in 0 1 2 3 4
do
    printf "====================3D full-resolution U-Net: fold $f===================="
    nnUNet_train 3d_fullres nnUNetTrainerV2 Task011_rmyy $f --npz
done

# 3D low resolution U-Net
for f in 0 1 2 3 4
do
    printf "====================3D low-resolution U-Net: fold $f===================="
    nnUNet_train 3d_lowres nnUNetTrainerV2 Task011_rmyy $f --npz
done

# 3D cascade U-Net
for f in 0 1 2 3 4
do
    printf "====================3D cascade U-Net: fold $f===================="
    nnUNet_train 3d_cascade_fullres nnUNetTrainerV2 Task011_rmyy $f --npz
done

