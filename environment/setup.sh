##############################
#     For Ubuntu 20.04       #
#  Usage : sudo sh setup.sh  #
##############################

sudo apt-get update -y

##############################
#           Misc             #
##############################

# Git
apt install git

# curl
sudo apt install curl

# Python2
apt install python2

# pip
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python2 get-pip.py

# Ruby
sudo apt-get install libreadline-dev
sudo apt install build-essential libssl-dev zlib1g-dev
git clone https://github.com/rbenv/rbenv.git ~/.rbenv
git clone https://github.com/sstephenson/ruby-build.git ~/.rbenv/plugins/ruby-build
<< BASHRC # append to .bashrc
export PATH=$PATH:$HOME/.rbenv/bin 
BASHRC
rbenv install 2.7.1

# docker
sudo apt install docker-compose
## for WSL
## https://docs.docker.com/engine/install/ubuntu/ Install Docker Engine 1

##############################
#           Pwn              #
##############################

# pwntools
python3 -m pip install pwntools

##############################
#         Reversing          #
##############################

# angr (with virtualenv)
apt-get install python3-dev libffi-dev build-essential virtualenvwrapper
<< BASHRC # append to .bashrc
### Virtualenvwrapper
if [ -f /usr/share/virtualenvwrapper/virtualenvwrapper.sh ]; then
    export WORKON_HOME=$HOME/.virtualenvs
    source /usr/share/virtualenvwrapper/virtualenvwrapper.sh
fi
BASHRC
# :after restart
mkvirtualenv --python=$(which python3) angr
pip install angr

# UPX
sudo apt-get install -y upx

# gdb-peda
git clone https://github.com/longld/peda.git ~/peda
echo "source ~/peda/peda.py" >> ~/.gdbinit

# for 32bit ELF
apt-get install lib32z1

# Ghidra (include install dependencies)
wget https://download.java.net/java/GA/jdk11/9/GPL/openjdk-11.0.2_linux-x64_bin.tar.gz
tar xvf openjdk-11.0.2_linux-x64_bin.tar.gz
sudo mkdir /opt/java/
sudo mv jdk-11.0.2 /opt/java/
echo 'JAVA_HOME=/opt/java/jdk-11.0.2' >> ~/.bashrc
echo 'PATH=$JAVA_HOME/bin:$PATH' >> ~/.bashrc

# uncompyle6 (.pyc to .py)
pip install uncompyle6

##############################
#          Crypto            #
##############################

# Crypto
pip3 install pycrypto
pip install pycryptodome

# Msieve
sudo apt-get install build-essential libgmp3-dev zlib1g-dev libecm-dev
wget "http://downloads.sourceforge.net/project/msieve/msieve/Msieve%20v1.52/msieve152.tar.gz?r=&ts=1452107977&use_mirror=jaist" -O msieve152.tar.gz
tar xvf msieve152.tar.gz
cd msieve-1.52/
make all ECM=1

##############################
#           Math             #
##############################

# SageMath
apt-get install sagemath

##############################
#         Forensic           #
##############################

# Volatility (include install dependencies)
sudo apt install pcregrep libpcre++-dev
sudo apt install gcc python2.7-dev
pip install pycrypto
pip install distorm3==3.4.4
git clone https://github.com/volatilityfoundation/volatility.git
cd volatility/
sudo python2 setup.py build install

# Wireshark
sudo apt install wireshark

# aircrack-ng
sudo apt-get install aircrack-ng

# binwalk
sudo apt install binwalk

# Zsteg(Ruby)
sudo gem install zsteg

# StegCracker (https://github.com/Paradoxis/StegCracker)
pip3 install stegcracker

# fcrackzip
sudo apt-get install fcrackzip

# pkcrack
wget https://www.unix-ag.uni-kl.de/\~conrad/krypto/pkcrack/pkcrack-1.2.2.tar.gz
tar xzvf pkcrack-1.2.2.tar.gz
cd pkcrack-1.2.2/src
make

# john the ripper
git clone https://github.com/openwall/john.git
cd john/src
./configure && make
sudo ln -s $(pwd)/../run/zip2john /usr/local/bin

# mupdf, mutool
sudo apt install mupdf-tools

# QSSTV
sudo apt-get install qsstv
sudo apt install pavucontrol

# ffmpeg
sudo apt install ffmpeg

##############################
#            Web             #
##############################

# nmap
sudo apt install nmap

# lynx
sudo apt install lynx
