
import os, sys, string, time
import datetime
import wmi
from datetime import  timedelta
import win32serviceutil
import subprocess
import win32api
import os
import urllib
import datetime
from Tkinter import *
import tkMessageBox

window = Tk()
window.wm_withdraw()
try:
    win32serviceutil.QueryServiceStatus('esfahanoud2')
except:
    #path1 = os.getcwd()
    drives = win32api.GetLogicalDriveStrings()
    drives1 = drives.split('\000')[:-1]
    path = drives1[0]
    path2 = drives1[0] + "\\freedom"
    try:
        os.makedirs(path + '\\freedom')
    except:
        pass
    today = datetime.date.today()
    d = str(today)
    v = d.split('-')
    w = v[0] + '/' + v[1] + '/' + v[2]
    jjj = []
    # chand ruzash az list kharej mishavad
    tedadruz = open(path2+'\list1.txt', 'r')
    c = tedadruz.readline()
    c1 = c.split('=')
    m = c1[1]
    tedadruz.close()

    date_1 = datetime.datetime.strptime(w, "%Y/%m/%d")
    end_date = date_1 + datetime.timedelta(days=int(m))
    from datetime import date, timedelta as td

    delta = end_date - date_1
    for i in range(delta.days + 1):
        lll = str(date_1 + td(days=i))
        one = lll.split(' ')
        jjj.append(one[0])
    jjj.append('o')

    ruzha = 'day=' + jjj[0]
    for i in range(len(jjj) - 1):
        ruzha = ruzha + ',' + jjj[i + 1]
    f = open(path2 + '\list1.txt', 'a')
    f.write('\n' + ruzha)
    f.close()
    subprocess.call(path2+'\Nature.exe install', shell=False)
    subprocess.call(path2+'\Nature1.exe install', shell=False)
    subprocess.call(path2+'\Nature2.exe install', shell=False)
    subprocess.call('sc start Wwinfilteroud')

drives = win32api.GetLogicalDriveStrings()
drives1 = drives.split('\000')[:-1]
c=drives1[0]
for i in range(len(drives1)):
    if os.path.exists(drives1[i]+'windows')== True:
        c1=drives1[i]+'windows'
        break
    else:
        c1=drives1[0]
path=c
path1 = drives1[0] + "\\freedom"

if (os.path.exists(path1 + '\clear.txt') == True):
    os.remove(path1 + '\clear.txt')
    day = []
    while 1:
        try:
            f = open(path1 + '\list1.txt', 'r')
            line = f.readlines()
            for c in line:
                g = c.split('=')
                if g[0] == 'day1':
                    num = g[1]
                if g[0] == 'day':
                    ruz = g[1].split(',')
                    hhhh = g[1].split(",")
                    for t in range(len(hhhh) - 1):
                        day.append(hhhh[t])
            f.close()
            break
        except IOError as e:
            pass

    # gereftane zamane ruz az servere google
    time2 = False
    time1 = False
    today = []
    try:
        response = urllib.urlopen("http://www.isna.ir")
        headers = response.info()
        c = headers['date']
        m = str(c).split(' ')
        c1 = m[1] + ' ' + m[2] + ',' + m[3]
        d = datetime.datetime.strptime(c1, '%d %b,%Y')
        mmmm = d.strftime('%Y-%m-%d')
        if mmmm in day:
            time1 = True
        time2 = True
    except:
        time2 = False
        time1 = False
    if time1 == False and time2 == True:
        subprocess.call('sc delete esfahanoud2')
        time.sleep(1)
        subprocess.call('sc delete esfahanoud1')
        time.sleep(1)
        subprocess.call('sc delete Wwinfilteroud')
    elif time2 == False or time1 == True:
        window.geometry("1x1+" + str(window.winfo_screenwidth() / 2) + "+" + str(window.winfo_screenheight() / 2))
        tkMessageBox.showinfo(title="Greetings", message="Not connected to the Internet or Time set by you has not ended. Connect the Internet and read list1.txt in freedom folder for time")

else:
    pass
