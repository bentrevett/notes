# Ubuntu Set-up

### Last Updated: 2020-03-11

I made this guide as I had issues getting NVIDIA drivers working on Ubuntu. I wanted a set-up of steps I could follow exactly to get everything working, and a lot of the stuff I found online was out-of-date or missed steps.

The below steps cover going from a working Windows install to getting Ubuntu 20.04 with the latest NVIDIA drivers installed.

### Installing Ubuntu
- Get [Ubuntu 20.04](https://releases.ubuntu.com/20.04/) on a USB stick with [Rufus](https://rufus.ie/) using [this](https://ubuntu.com/tutorials/create-a-usb-stick-on-windows) guide.
- Plug the USB stick into the computer you want to install Ubuntu on. The rest of the steps are to be done on that computer.
- Press the Windows key and type 'advanced startup' and go to 'Change advanced startup options'
- Under 'Advanced startup' click 'Restart now'
- In the blue menu screen, click 'Advanced boot options' and choose your USB stick.
- Install Ubuntu following the steps from [here](https://ubuntu.com/tutorials/install-ubuntu-desktop#5-prepare-to-install-ubuntu). 
  - I always found it less error prone to erase disk and install Ubuntu. If you want to keep Windows, then don't do this.

### Installing NVIDIA Drivers
- These might have been installed during the Ubuntu installation, depending on your card. You should try them anyway.
- `ubuntu-drivers devices` should list the NVIDIA card and available drivers
- Install the default with `sudo ubuntu-drivers autoinstall` or manually choose one and install with `sudo apt install`
- As of 03/2021, version 460 is the latest and seems to work well
- Reboot machine and on restart try `nvidia-smi` which should correctly show the NVIDIA card's statistics

### CUDA
- `sudo apt install nvidia-cuda-toolkit`
- As of 03/2021, should install version 10.1
- Reboot machine and on restart try `nvcc --version`, should correctly show CUDA version

### Conda
- `wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh`
- `chmod +x Miniconda3-latest-Linux-x86_64.sh`
- `./Miniconda3-latest-Linux-x86_64.sh`
- Choose yes/OK to everything
- Create environment with `conda create -n <NAME> python=x.y` where `x.y` is the python version you want, currently the latest is 3.9 which you can get by just putting `python=3`.
- Activate environment with `conda activate <NAME>`
- Install packages with `conda install <PACKAGE(S)>`, for example: `conda install jupyter notebook matplotlib numpy`

### PyTorch
- Check https://pytorch.org for latest PyTorch installation instructions
- As of 03/2021, `pip install torch torchvision torchaudio torchtext`

### Git
- `sudo apt install git`
- `git config --global user.name "<USERNAME>"`
- `git config --global user.email "<EMAIL>"`

### Misc.
- Install anything else - Chrome, VSCode, Calibre - from the browser

### Latex
- `sudo apt install texlive-full`
- `sudo apt install texstudio`
