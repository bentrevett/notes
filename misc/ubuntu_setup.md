# Ubuntu Set-up

### Ubuntu
- Get [Ubuntu](https://releases.ubuntu.com/20.04/) on a USB stick with [Rufus](https://rufus.ie/)
- Plug the USB stick into the PC and reboot
- As the computer boots, press F2 to open the boot menu
- Choose to boot from the UEFI version of the USB stick
- Preferrably use the option to erase the disk and install

### NVIDIA
- `ubuntu-drivers devices` should list the NVIDIA card and available drivers
- Install the default with `sudo ubuntu-drivers autoinstall` or manually choose one and install with `sudo apt install`
- As of 07/2020, version 440 is the latest and seems to work well
- Reboot machine and on restart try `nvidia-smi` which should correctly show the NVIDIA card's statistics

### CUDA
- `sudo apt install nvidia-cuda-toolkit`
- As of 07/2020, should install version 10.1
- Reboot machine and on restart try `nvcc --version`, should correctly show CUDA version

### Conda
- `wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh`
- `chmod +x Miniconda3-latest-Linux-x86_64.sh`
- `./Miniconda3-latest-Linux-x86_64.sh`
- Choose yes/OK to everything
- Create environment with `conda create -n <NAME> python=x.y` where `x.y` is the python version you want, currently the latest is 3.8
- Activate environment with `conda activate <NAME>`
- Install packages with `conda install <PACKAGE(S)>`, for example: `conda install jupyter notebook matplotlib numpy`

### PyTorch
- Check https://pytorch.org for latest PyTorch installation instructions
- As of 07/2020, `conda install pytorch torchvision cudatoolkit=10.1 -c pytorch`

### Git
- `sudo apt install git`
- `git config --global user.name "<USERNAME>"`
- `git config --global user.email "<EMAIL>"`

### Misc.
- Install anything else - Chrome, VSCode, Calibre - from the browser

### Latex
- `sudo apt install texlive-full`
- `sudo apt install texstudio`