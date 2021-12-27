# Load Sharing Facility (LSF) by IBM
LSF is a resource cluster management system developed by IBM. In our lab, LSF manages and distributes GPU resources. 

## What's in our cluster:
cuda10.1, cuda9.0, anaconde3, python3.6, python3.7, pytorch

## How to use the cluster:
> $ bsub < job_sub.sh // 提交任务 <br/>
> $ jjobs // 查看自己所有的任务情况 <br/>
> $ jjobs -u all //查看所有的任务详细情况<br/>
> $ jjobs -l JOBID //查看JOBID这个任务的详细情况<br/>
> $ jctrl kill JOBID //终止某个任务<br/>
> $ jqueues //查看所有队列的状态<br/>
> $ jsub -q queue_name task.sh //提交任务到特定队列<br/>
> $ jctrl stop JOBID //暂停某个任务<br/>
> $ jctrl resume JOBID //恢复某个任务<br/>
> $ jhosts // 查看节点信息 <br/>
> 
## Understand the relation between "local" virtual environment and the cluster:
1. Users can create their own virtual environment based on this [instruction](https://github.com/ruiyangqin2016/rmyy_medical_segmentation/blob/main/documents/How_to_use_remote_server.md). <br />
2. Users should install every library they need under their virtual environment. **But keep in mind**, even if the user activate virtual environment, the cluster will not activate your local virtual environment automatically when it receives a job request. <br />
3. In the script, the user should add the command line which he/she uses to activate virtual environment. <br/>
"$ source /environment/folder/bin/activate"  (Just like line 38 in [job_sub.sh](https://github.com/ruiyangqin2016/rmyy_medical_segmentation/blob/main/job_sub.sh)) And then write commands to execute. <br/>
