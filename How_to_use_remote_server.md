## How to use the lab server:
1. login:
> $ ssh ruiyang@183.236.15.122 -p 20016
>
> password: Rmyy_123456
>
2. Activate Anacoda3 environment:
> $ source /data/users/software/anaconda3/bin/activate
>
3. Make dir and go
> $ mkdir *environment_name*
> 
> $ cd *environment_name*
>
4. Create virtual environment 
> $ python -m venv *project_name*
> 
5. Activate virtual environment (Start from this step if you are a returned user)
> $ source ./*environment_name*/bin/activate

## What to install (Under virtual environment):
> $ pip install nnunet
> 
> $ pip3 install torch==1.10.1+cu113 torchvision==0.11.2+cu113 torchaudio==0.10.1+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html

## Upload file to the server:
> $ scp -P *Address_of_File* username@IP_address: *Target_Server_Location*
> 
> For example: scp -P xxxx /home/ruiyang/Desktop/nnUNet/data.json ruiyang@xxx.xxx.xxx.xxx:/data/users/ruiyang/nnUNet/nnUNet_raw/nnUNet_raw_data
> 
> Note: port identifier is uppercase instead of lowercase.

## Notes:
> $ pwd // show current location in the server
> 
> Once activate vitrual environment, use pip to install any package you want if "conda install" doesn't work properly
