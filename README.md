
<p align="center">
  <img width="410" height="410" src="https://raw.githubusercontent.com/STRT-Official/storage-plant/a33f89f0b8a3b3c7b545c71dd46929fd552e1218/LOGO.svg">
</p>


# Ketta ..Yet another virtual assistant

Dear developers, 
              <p>This is not a public stable release, so you may face some bugs.</p>
              
# Installation

Important note!!! : This build only works on linux(preferably arch) but we will soon port it to other OSes (windows is in progress.

Requiremets : wget, unzip(this is mosly preinstalled in all linux distros) and docker(if you want to do speech syntheses)

`git clone https://github.com/STRT-Official/Ketta-Official`

`cd Ketta-Official`

`python setup.py`

# Wake-Word module 

We use a method called `transfer learning`. It means that we already have a pre-trained model , which can be expanded further.

Visualization of the wake-word-recog current model :

<p align="center">
  <img width="410" height="1000" src="https://raw.githubusercontent.com/STRT-Official/storage-plant/main/model_visualized.png">
</p>

# Using

simply run the `vad.py` file.

Disclaimer : There are situations when the vad.py file will not close when you press ctrl+c. In that case, please close that terminal 
and use a new one.

This is the official, though strtsnm has a own repo of this. Tested and stable releases will be uploaded here. For beta versions , please visit : https://github.com/STRTSNM/Ketta
