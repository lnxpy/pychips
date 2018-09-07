from os import system as sys
from time import sleep as slp
from platform import system
from clr import colors as clr

def loading(delay,txt):
    os = system()
    ctype = {'Windows':'cls','Linux':'clear'}
    color = {'0':0,'1':51,'2':102,'3':153,'4':204,'5':255}

    for i in range(delay):
        sys(ctype[os])
        print()
        print('🌖 | Loading | 🌍')
        print('\n'+clr.yellow+'Rep'+clr.end+' : '+txt)
        slp(.3)
        sys(ctype[os])
        print()
        print('🌗 -| Loading |- 🌎')
        print('\n'+clr.yellow+'Rep'+clr.end+' : '+txt)
        slp(.3)
        sys(ctype[os])
        print()
        print('🌘 --| Loading |-- 🌍')
        print('\n'+clr.yellow+'Rep'+clr.end+' : '+txt)
        slp(.3)
        sys(ctype[os])
        print()
        print('🌚 ---| Loading |--- 🌎')
        print('\n'+clr.yellow+'Rep'+clr.end+' : '+txt)
        slp(.3)
    return 0
