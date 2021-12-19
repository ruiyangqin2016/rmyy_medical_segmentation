## How to use the lab server:
1. login:
> $ ssh ruiyang@183.236.15.122 -p 20016
>
> password: Rmyy_123456
>
2. Activate Anacoda3 environment:
> $ cd ./software
> 
> $ source anaconda3/bin/activate
>
3. Create user's own virtual environment
> $ conda create -n *my_virtual_environment(name whatever you want)* python=3.7
>
4. Activate virtual environment (Start from this step if you are a returned user)
> $ conda activate *my_virtual_environment*

## What to install (Under virtual environment):
> $ pip install nnUNet
> 
> $ conda install -c anaconda cudatoolkit=11.3
> 
> $ conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch
> 
> Note: If conda doesn't work, use pip.

## Upload file to the server:
> $ scp -P *Address_of_File* username@IP_address: *Target_Server_Location*
> 
> For example: scp -P xxxx /home/ruiyang/Desktop/nnUNet/data.json ruiyang@xxx.xxx.xxx.xxx:/data/users/ruiyang/nnUNet
> .
> Note: port identifier is uppercase instead of lowercase.
