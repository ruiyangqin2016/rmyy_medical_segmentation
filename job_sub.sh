#!/bin/bash 
#JSUB -J ruiyang
#JSUB -q tensorflow_sub
#JSUB -gpgpu "num=2" 
#JSUB -R "span[ptile=2]" 
#JSUB -n 2
#JSUB -o output.%J 
#JSUB -e err.%J 
 
##########################Cluster environment variable###################### 
if [ -z "$LSB_HOSTS" -a -n "$JH_HOSTS" ]
then
        for var in ${JH_HOSTS}
        do
                if ((++i%2==1))
                then
                        hostnode="${var}"
                else
                        ncpu="$(($ncpu + $var))"
                        hostlist="$hostlist $(for node in $(seq 1 $var);do printf "%s " $hostnode;done)"
                fi
        done
        export LSB_MCPU_HOSTS="$JH_HOSTS"
        export LSB_HOSTS="$(echo $hostlist|tr ' ' '\n')"
fi

nodelist=.hostfile.$$
for i in `echo $LSB_HOSTS`
do
    echo "${i}" >> $nodelist
done

ncpu=`echo $LSB_HOSTS |wc -w`
##########################Software environment variable##################### 
module load cuda/cuda10.1 
module load pytorch/pytorch1.5.1 
##########################Software run command############################## 
source /data/users/ruiyang/environments/nnunet/bin/activate

## 2D U-Net
nnUNet_train 2d nnUNetTrainerV2 Task011_rmyy 0 --npz >> log_2D_0.txt
##nnUNet_train 2d nnUNetTrainerV2 Task011_rmyy 1 --npz >> log_2D_1.txt
##nnUNet_train 2d nnUNetTrainerV2 Task011_rmyy 2 --npz >> log_2D_2.txt
##nnUNet_train 2d nnUNetTrainerV2 Task011_rmyy 3 --npz >> log_2D_3.txt
##nnUNet_train 2d nnUNetTrainerV2 Task011_rmyy 4 --npz >> log_2D_4.txt