# Tetralog of Fallot (TOF)
<img src=https://github.com/ruiyangqin2016/rmyy_medical_segmentation/blob/main/documents/images/tof_1.jpeg width=40% height=auto> <img src=https://github.com/ruiyangqin2016/rmyy_medical_segmentation/blob/main/documents/images/tof_2.jpeg width=auto height=277><br/>

## Introduction
法洛四联症由A. Fallot医生提出。总共有四种情况构成了此疾病：<br/>
1. 肺动脉(pulmonary artery)，肺动脉瓣(pulmonary valve)或右心室(RV-right ventricle)漏斗部(Infundibulum)狭窄 <br/>
2. 主动脉口(aortic orifice)跨位(amphi-position)在左右心室 <br/>
3. 心室中隔(atrioventricular septum)缺损 <br/>
4. 右心室肥大(Right ventricular hypertrophy) <br/>
5. (附加)只有心室间隔缺损、肺动脉口狭窄和右心室肥大而无法主动脉骑跨的病人，成为非典型性法洛四联症

## Measurements
### 1. 左右心室面积
**如何测量**：选择轴位面，在左右心室最长的层面，分别测量左右心室的长径（即左右心室从顶端到心尖的长度）和横径（即左右心室从左到右的长度），以及左右心室的面积。Feel free to watch this in [video](https://www.youtube.com/watch?v=uadEfbf3ZxA). <br/>
<img src=https://github.com/ruiyangqin2016/rmyy_medical_segmentation/blob/main/documents/images/RV_LV/tof_2.png width=43% height=auto>
<img src=https://github.com/ruiyangqin2016/rmyy_medical_segmentation/blob/main/documents/images/RV_LV/tof_4.gif width=27% height=auto>
<img src=https://github.com/ruiyangqin2016/rmyy_medical_segmentation/blob/main/documents/images/RV_LV/tof_5.jpg width=28% height=auto> <br/>


### 2. 左肺静脉面积
**肺静脉**： 人体肺部分为5叶，肺静脉实际上也分为5支，分别是左上肺静脉，左下肺静脉，右上肺静脉，右中肺静脉和右下肺静脉，供应不同的肺叶，在CT中右上肺静脉和右中肺静脉通常汇聚为1条静脉，即在左心房入口处可见1肺静脉，往下浏览可见右中和右上静脉分出，通常肺静脉只能测量到4条静脉，分别是左上肺静脉，左下肺静脉，右上肺静脉与右中肺静脉汇聚为1条的肺静脉，以及右下肺静脉。<br/>
**如何测量**：以左肺静脉为例，定位到轴位面，可以看到左心房与左肺静脉的结构，在左肺静脉汇入左房前5mm处定位，转至矢状面，调整轴面和冠状面的角度，与肺静脉垂直即可，此时矢状面的肺静脉近似圆形，即可测量得到左肺静脉的面积。其他肺静脉测量原理相同。Feel free to watch this [video](https://www.youtube.com/watch?v=zszUlJ3y96I)<br/>
<img src=https://github.com/ruiyangqin2016/rmyy_medical_segmentation/blob/main/documents/images/PA/tof_6.png width=32.5%>
<img src=https://github.com/ruiyangqin2016/rmyy_medical_segmentation/blob/main/documents/images/PA/tof_7.png width=32.5%>
<img src=https://github.com/ruiyangqin2016/rmyy_medical_segmentation/blob/main/documents/images/PA/tof_8.png width=32.5%>

### 3. 主动脉面积
**关键词解释**：
1. Valsalva窦(主动脉窦dou，英文：Aortic Sinus)：主动脉瓣相对的动脉壁向外膨出，瓣膜与主动脉壁之间的内腔，称主动脉窦或瓦耳萨耳瓦窦(Val-salvaantrum)，简称瓦氏窦。<br/>
<img src=https://github.com/ruiyangqin2016/rmyy_medical_segmentation/blob/main/documents/images/AS/tof_9.jpeg width=70%><img src=https://github.com/ruiyangqin2016/rmyy_medical_segmentation/blob/main/documents/images/AS/tof_10.jpeg width=25%><br/>
2. **S**ino**t**ubular **J**unction (STJ): The sinotubular junction is the region of the ascending aorta between the aortic sinuses (of Valsalva) and where the normal tubular configuration of the aorta is attained. It marks the junction of the aortic root and ascending aorta. <br/>
<img src=https://github.com/ruiyangqin2016/rmyy_medical_segmentation/blob/main/documents/images/AS/tof_11.jpeg width=40%><img src=https://github.com/ruiyangqin2016/rmyy_medical_segmentation/blob/main/documents/images/AS/tof_12.png width=50%><br/>

**主动脉**：此为主动脉根部位置，LOVT为左心室流出道。此项指标通常用于升主动脉瘤和A型夹层，但TOF患者往往也会合并主动脉根部扩张，故此指标也纳入。<br/>

**测量方法**：定位于冠状面，旋转此平面直至主动脉根部完全显露，从上至下分别是STJ（窦管交界），主动脉valsalva窦和主动脉瓣环直径（SOV）。<br/>
<img src=https://github.com/ruiyangqin2016/rmyy_medical_segmentation/blob/main/documents/images/AS/tof_13.jpg width=23%><img src=https://github.com/ruiyangqin2016/rmyy_medical_segmentation/blob/main/documents/images/AS/tof_14.png width=29%> <br/>

### 4. 主瓣各瓣叶周长
**如何测量**：定位于轴位面，找到左室流出道（LVOT）进入主动脉后的位置，此时的主动脉瓣看不到LVOT，也没有发出冠状动脉，定位于主动脉瓣后，调整冠状面和矢状面至垂直，此时可以清晰地看见主动脉瓣的三叶结构，在此时测量主动脉瓣环直径（SOV），主动脉瓣面积，主动脉瓣叶周长，瓣叶窦-窦长径，瓣叶窦-连合长径。所有主动脉瓣的测量均在此处进行。<br/>
<img src=https://github.com/ruiyangqin2016/rmyy_medical_segmentation/blob/main/documents/images/ML/tof_15.png width=43%><img src=https://github.com/ruiyangqin2016/rmyy_medical_segmentation/blob/main/documents/images/ML/tof_16.jpg width=29%> <br/>






### 缩写词表
>AAS = Acute aortic syndrome 急性主动脉综合征<br/>
AR = Aortic regurgitation 主动脉瓣反流<br/>
ASE = American Society of Echocardiography 美国超声心动图学会<br/>
BAI = Blunt aortic injury 主动脉钝性损害<br/>
BSA = Body surface area 体表面积<br/>
CT = Computed tomography 计算机断层扫描<br/>
CTA = Computed tomographic aortography CT 主动脉造影成像<br/>
CXR = Chest x-ray 胸部 X 线<br/>
EACVI = European Association of Cardiovascular Imaging 欧洲心血管影像学会<br/>
EAU = Epiaortic ultrasound 主动脉外超声<br/>
GCA = Giant-cell (temporal) arteritis 巨细胞性 (颞) 动脉炎<br/>
ICM = Iodinated contrast media 碘造影剂<br/>
IMH = Intramural hematoma 壁内血肿<br/>
IRAD = International Registry of Acute Aortic Dissection 急性主动脉夹层的国际注册<br/>
MDCT = Multidetector computed tomography 多排探测器螺旋 CT <br/>
MIP = Maximum-intensity projection 最高强度投影<br/>
MR = Magnetic resonance 磁共振<br/>
MRI = Magnetic resonance imaging 磁共振成像<br/>
PWV = Pulsewave velocity 脉搏波传播速度<br/>
STJ = Sinotubular junction 窦管交界处<br/>
TA = Takayasu arteritis 多发性动脉炎<br/>
TEE = Transesophageal echocardiography 经食管超声心动图<br/>
TEVAR = Transthoracic endovascular aortic repair 经胸血管内主动脉修复<br/>
3D = Three-dimensional 三维<br/>
TTE = Transthoracic echocardiography 经胸超声心动图<br/>
2D = Two-dimensional 二维<br/>
ULP = Ulcerlike projection 溃疡样投影<br/>


### 引用
> 1. [2015 成人胸主动脉疾病多方法成像](https://www.asecho.org/wp-content/uploads/2016/06/MM-Imaging-in-Thoracic-Aortic-Diseases-2015_Chinese.pdf)
