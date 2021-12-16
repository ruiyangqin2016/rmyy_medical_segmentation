# rmyy_medical_segmentation

## Data process
1. Your dataset should have each pair of image and label file named same except for their tails. For the image file, it should be named by xxx_image.nii.gz; for the label file, it should be named by yyy_label.nii.gz; and xxx == yyy.
2. Set your dataset address as the value of variable *files_address* in [rename.py](https://github.com/ruiyangqin2016/rmyy_medical_segmentation/blob/main/rename.py).
3. Run [rename.py](https://github.com/ruiyangqin2016/rmyy_medical_segmentation/blob/main/rename.py) to update every file in your dataset. You will also receive a log file to track between original name and changed name. The log file will be saved under the same location of your rename.py file.
4. Each file in your dataset should be *nii.gz* file.
5. Run [generate_nii_gz.py](https://github.com/ruiyangqin2016/rmyy_medical_segmentation/blob/main/generate_nii_gz.py) to update your dataset. Also, remember to change directory variable in *generate_nii_gz.py* file.
6. Run [generate_json.py](https://github.com/ruiyangqin2016/rmyy_medical_segmentation/blob/main/generate_json.py) to generate your own json file. This file is called *dataset.json*, located in your dataset folder. Also, remember to change directory variable in *generate_json.py* file.

## Run in virtual environment
After finish data processing, the next step is to setup virutal environment. The detail instruction could be found [here](https://linoxide.com/linux-how-to/setup-python-virtual-environment-ubuntu/)

Install virtual environment(virtualenv)
> $ sudo apt-get install -y python3-venv
>
Make a new directory
> $ mkdir *environments_name*
>
> $ cd *environments_name*
>
Create an environment
> $ python3 -m venv *project_name*
>
Install nnUNet from [Fabian's github](https://github.com/MIC-DKFZ/nnUNet) by following the instructions 
> $ pip3 install nnUNet
> 
Activate the virtual environment
> $ source *project_name*/bin/activate
