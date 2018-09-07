# I don't say nothing!
# Just read the Readme.txt

#{
from clr import colors as clr
from log import login
from loader import loading
from cv2 import imread as reader , imwrite as writer
from numpy import array as arr
from socket import gethostname as username
from os import system as sys
from time import sleep as slp
from platform import system
from datetime import datetime as time
#}
os = system()
ctype = {'Windows':'cls','Linux':'clear'}
color = {'0':0,'1':51,'2':102,'3':153,'4':204,'5':255}

if system() == 'Linux':
    di = '/'
elif system() == 'Windows':
    di = '\\'

def main():
    login('running pychips',username())
    sys(ctype[os])
    print('\n<~~ Welcome to Pychips ~~>\n')
    print(clr.yellow+'Rep'+clr.end+' : First,'+clr.red+' Read'+clr.end+' the '+clr.bold+'Readme.txt!'+clr.end)
    print(clr.yellow+'Rep'+clr.end+' : All Modules Imported'+clr.green+' Successfully!'+clr.end)

    qt = input(clr.yellow+'Qt '+clr.end+': Would you want to Show the Readme.txt (y/n) : ')
    print()
    if qt == 'Y' or qt == 'y':
        print('\n'+readme())
    flict()


def flict():
    pic = arr([])
    input(clr.yellow+'Rep'+clr.end+' : Press Enter to'+clr.green+' Start'+clr.end+' Pychips..')
    loading(3,'Please Wait for Loading Datas..')
    sys(ctype[os])
    print('\n'+clr.yellow+'Rep'+clr.end+' : All Datas Loaded'+clr.green+' Successfully!'+clr.end)
    print(clr.yellow+'Rep'+clr.end+' : Your Picture : '+clr.end,end='')
    print(pic)

    qt = int(input('\n'+clr.yellow+'Qt '+clr.end+': Enter the range (2,4,6,8) : '))

    if qt!=2 and qt!=4 and qt!=6 and qt!=8:
        print(clr.red+'Err'+clr.end+' : Invalid Value!')
        return

    sys(ctype[os])
    pic = arr([[0]*qt]*qt)
    while True:
        print('\n'+clr.yellow+'Rep'+clr.end+' : Your Picture : '+clr.end+'\n')
        for i in pic:
            print(i)

        print(clr.yellow+'\nRep'+clr.end+' : Now you can Change the Values by 0 to 5.\nPattern : [x,y]=v or q')
        qt = input(clr.yellow+'\ninput'+clr.end+' : ')
        if qt == 'q' or qt == 'Q':
            break
        elif qt[0] != '[' and qt[len(qt)-1] != ']':
            sys(ctype[os])
            continue
        else:
            x = qt[1]
            y = qt[3]
            v = qt[-1]
            exec('pic[{},{}]={}'.format(x,y,color[str(v)]))
        sys(ctype[os])

    tpp = '.'+input(clr.yellow+'Qt '+clr.end+': Enter the picture type ( png , jpg , jpeg ) : ')
    if tpp == '.png' or tpp == '.jpeg' or tpp == '.jpg':
        input(clr.yellow+'Rep'+clr.end+' : Press Enter to'+clr.green+' Rendering '+clr.end+'the `'+username()+tpp+'`..')
        loading(5,'Start Rendering..')
        writer('pic'+di+username()+tpp,pic)
        print(clr.yellow+'Rep'+clr.end+' : Rendering has'+clr.green+' Finished!')
        slp(2)
        print(clr.yellow+'Rep'+clr.end+' : Please check the '+clr.green+di+'pic'+clr.end+' Directory!')
        print(clr.yellow+'Rep'+clr.end+' :  '+clr.green+di+'pic'+clr.end+' Directory!')
        # asking do you want to show picture??
        login('rendering pic'+di+username()+tpp,username())
        qt = input(clr.yellow+'Qt '+clr.end+': Would you like to show your picture (y/n) : ')
        if qt == 'y' or qt=='Y':
            if os == 'Linux':
                try:
                    sys('gnome-open pic/'+username()+tpp)
                    login('opening pic'+di+username()+tpp,username())
                except:
                    print(clr.red+'Err'+clr.end+' : Available only for Gnome-Desktop!')
            elif os == 'Windows':
                try:
                    sys('pic\\'+username()+tpp)
                    login('opening pic'+di+username()+tpp,username())
                except:
                    print(clr.red+'Err'+clr.end+' : Faild to open the picture!')
                    login('faild to open the picture'+di+username()+tpp,username())

        input(clr.yellow+'Rep'+clr.end+' : Press enter to exit the '+clr.green+'Pychips..'+clr.end)
    else:
        print(clr.red+'Err'+clr.end+' : Invalid Value!')

def show():
    print('SHOING PICTURE!')

def readme():
    file = open('Readme.txt','r')
    content = clr.red+'<'+clr.end+'Readme'+clr.red+'>'+clr.end+'\n'+file.read()
    return content

if __name__ == '__main__':
    main()
