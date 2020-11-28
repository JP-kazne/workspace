##############################
#     For Ubuntu 20.04       #
#  Usage : sudo sh setup.sh  #
##############################

##############################
#           Misc             #
##############################

# Git
apt install git

# Python2
apt install python2

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

# gdb-peda
git clone https://github.com/longld/peda.git ~/peda
echo "source ~/peda/peda.py" >> ~/.gdbinit

# for 32bit ELF
apt-get install lib32z1

##############################
#          Crypto            #
##############################

# Crypto
pip3 install pycrypto

##############################
#           Math             #
##############################

# SageMath
apt-get install sagemath