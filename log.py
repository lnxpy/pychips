# log.py is for writing logs in log.txt

#{
from datetime import datetime as time
from platform import system as sys
#}
def login(stat,user):

    file = open('log.txt','a')
    file.write(stat+' from '+user+' user'+' on '+sys()+' os <~~~> '+str(time.now())+'\n')
    file.close()
