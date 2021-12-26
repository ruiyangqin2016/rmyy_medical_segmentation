# Load Sharing Facility (LSF) by IBM
LSF is a resource cluster management system developed by IBM. In our lab, LSF manages and distributes GPU resources. 

## What's in our cluster:
cuda10.1, cuda9.0, anaconde3, python3.6, python3.7, pytorch

## How to use the cluster:
> $ bsub < job_sub.sh
> 
## Understand the relation between "local" virtual environment and the cluster:
1. Users can create their own virtual environment based on this [instruction](https://github.com/ruiyangqin2016/rmyy_medical_segmentation/blob/main/documents/How_to_use_remote_server.md). <br />
2. Users should install every library they need under their virtual environment. **But keep in mind**, even if the user activate virtual environment, the cluster will not activate your local virtual environment automatically when it receives a job request. <br />
3. In the script, the user should add the command line which he/she uses to activate virtual environment. (Just like line 38 in [job_sub.sh](https://github.com/ruiyangqin2016/rmyy_medical_segmentation/blob/main/job_sub.sh)) And then write commands to execute.
