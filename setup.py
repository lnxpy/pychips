# this is the setup script for Pychips
# check your connection then Run this script befor running the Pychps.py
# Don't run this script, If you Installed the opencv-python and numpy
# You must installed the python3-pip package

#{
from os import system as sys
from platform import system as os
from clr import colors as clr
#]

print('<~~ Welcome to Pychips Installer ~~>\n')

input(clr.yellow+'Rep'+clr.end+' : Press Enter to Complete the Modules Installation..')

try:
    sys('pip3 install opencv-python')
except Exception as e:
    print('\n> Check you''r Connection')
    print('\n> Check you''r pip Version it must be 3')
    print('\n> Then try again')
