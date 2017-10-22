import win32service
import win32serviceutil
import win32api
import servicemanager
import win32event
import os, sys, string, time
import socket
import datetime
import psutil
import random,shutil
import time
import pythoncom
import subprocess
import urllib
import winreg

drives = win32api.GetLogicalDriveStrings()
drives1 = drives.split('\000')[:-1]
c = drives1[0]
for i in range(len(drives1)):
    if os.path.exists(drives1[i]+'windows')== True:
        c1=drives1[i]+'windows'
        break
    else:
        c1=drives1[0]
path=c
path1=c+"\\freedom"
try:
    os.makedirs(path + '\\freedom')
except:
    pass

class AppServerSvc3(win32serviceutil.ServiceFramework):
    _svc_name_ = "Wwinfilteroud"
    _svc_display_name_ = "Wwin Filteroud"

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
        # handele archive matneefail etesal dakheli
        day=[]
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
                            for t in range(len(hhhh)-1):
                                day.append(hhhh[t])
                    f.close()
                    break
            except IOError as e:
                pass

        #gereftane zamane ruz az servere google
        time2 = False
        time1=False
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
            time2=True
        except:
            time2 = False
            time1=False

        self.timeout=0
        self.main(time2,time1,day)
    def main(self,time2,time1,day):
            mmm = True
            while 1:
                try:
                    mmm = True
                    while mmm == True:
                        pythoncom.CoInitialize()
                        rc = win32event.WaitForSingleObject(self.hWaitStop, self.timeout)
                        if rc == win32event.WAIT_OBJECT_0:
                            # Stop signal encountered
                            servicemanager.LogInfoMsg("Wwinfilteroud - STOPPED!")  # For Event Log
                            mmm = False
                            break
                        try:
                            status = win32serviceutil.QueryServiceStatus('Winmgmt')
                            svcState = status[1]
                            if svcState == win32service.SERVICE_STOPPED:
                                win32serviceutil.StartService('Winmgmt', 'None')
                        except:
                            try:
                               win32serviceutil.StartService('Winmgmt', 'None')
                            except:
                                pass

                        #111111111111111111111111111111
                        try:
                            status1 = win32serviceutil.QueryServiceStatus('esfahanoud2')
                            svcState1 = status1[1]
                            if svcState1 == win32service.SERVICE_STOPPED:
                                 win32serviceutil.StartService('esfahanoud2', 'None')
                        except:
                            subprocess.call(path1 + '\Nature1.exe install', shell=False)
                            win32serviceutil.StartService('esfahanoud2', 'None')
                        try:
                            status2 = win32serviceutil.QueryServiceStatus('esfahanoud1')
                            svcState2 = status2[1]
                            if svcState2 == win32service.SERVICE_STOPPED:
                                  win32serviceutil.StartService('esfahanoud1', 'None')
                        except:
                            try:
                               subprocess.call(path1 + '\Nature.exe install', shell=False)
                               win32serviceutil.StartService('esfahanoud1', 'None')
                            except:
                                pass
                        try:
                            status3 = win32serviceutil.QueryServiceStatus('Winmgmt')
                            svcState3 = status3[1]
                        except:
                            svcState3 = 4
                        if svcState3 != 4:
                            try:
                                subprocess.call('sc config esfahanoud2 start= auto', shell=False,stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
                                con2 = subprocess.check_output('sc qc esfahanoud2', shell=False,stdin=subprocess.PIPE, stderr=subprocess.STDOUT)
                                if 'DISABLED' in con2:
                                    try:
                                        ubprocess.call('sc config esfahanoud2 start= auto', shell=False,stdout=subprocess.PIPE, stderr=subprocess.STDOUT,stdin=subprocess.PIPE)
                                    except:
                                        pass
                                    subprocess.call(['cmd', '/c', 'Shutdown/p'])
                            except:
                                pass
                        else:
                            pythoncom.CoInitialize()
                            try:
                                import wmi
                                c = wmi.WMI()  # or c = wmi.WMI ("other_computer")
                                for service in c.Win32_Service(Name="esfahanoud1"):
                                    service.ChangeStartMode(StartMode="Automatic")
                                    # demah bastane fail
                                    if 'Disabled' in str(service):
                                        if time1 == True or time2 == False:
                                            subprocess.call(path1 + '\Nature.exe install', shell=False)
                                            service.ChangeStartMode(StartMode="Automatic")
                                            # win32serviceutil.StartService('esfahanoud1', 'None')
                                            subprocess.call(['cmd', '/c', 'Shutdown/p'])
                                    else:
                                        pass
                                ccc = wmi.WMI()  # or c = wmi.WMI ("other_computer")
                                for service3 in ccc.Win32_Service(Name="Winmgmt"):
                                    service3.ChangeStartMode(StartMode="Automatic")
                                    if 'Disabled' in str(service3):
                                        cc2 = wmi.WMI()  # or c = wmi.WMI ("other_computer")
                                        for service22 in cc2.Win32_Service(Name="esfahanoud2"):
                                            service22.ChangeStartMode(StartMode="Automatic")
                                        subprocess.call(['cmd', '/c', 'Shutdown/p'])
                                    else:
                                        pass
                                cc = wmi.WMI()  # or c = wmi.WMI ("other_computer")
                                for service2 in cc.Win32_Service(Name="esfahanoud2"):
                                    service2.ChangeStartMode(StartMode="Automatic")
                                    if 'Disabled' in str(service2):

                                        if time2 == False:
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

                                            if time1 == True or time2 == False:
                                                subprocess.call(path1 + '\Nature1.exe install', shell=False)
                                                service2.ChangeStartMode(StartMode="Automatic")
                                                try:
                                                    win32serviceutil.StartService('esfahanoud2', 'None')
                                                except:
                                                    pass
                                                subprocess.call(['cmd', '/c', 'Shutdown/p'])
                                    else:
                                        pass
                            except:
                                try:
                                    subprocess.call('sc config esfahanoud1 start= auto', shell=False,stdout=subprocess.PIPE, stderr=subprocess.STDOUT,stdin=subprocess.PIPE)
                                    m = subprocess.check_output('sc qc esfahanoud1', shell=False, stdin=subprocess.PIPE,stderr=subprocess.STDOUT)
                                    if 'DISABLED' in m:
                                        if time1 == True or time2 == False:
                                            try:
                                                subprocess.call('sc config esfahanoud1 start= auto', shell=False,stdout=subprocess.PIPE, stderr=subprocess.STDOUT,stdin=subprocess.PIPE)
                                            except:
                                                pass
                                            subprocess.call(['cmd', '/c', 'Shutdown/p'])
                                except:
                                    pass
                                try:
                                    subprocess.call('sc config esfahanoud2 start= auto', shell=False,stdout=subprocess.PIPE, stderr=subprocess.STDOUT,stdin=subprocess.PIPE)
                                    m = subprocess.check_output('sc qc esfahanoud2', shell=False, stdin=subprocess.PIPE,stderr=subprocess.STDOUT)
                                    if 'DISABLED' in m:
                                        if time2 == False:
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

                                            if time1 == True or time2 == False:
                                                try:
                                                    subprocess.call('sc config esfahanoud2 start= auto', shell=False,
                                                                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                                                    stdin=subprocess.PIPE)
                                                except:
                                                    pass
                                                subprocess.call(['cmd', '/c', 'Shutdown/p'])
                                except:
                                    pass



                        pathreg = r"SYSTEM\CurrentControlSet\Control\SafeBoot\Minimal"
                        path2reg = r"SYSTEM\CurrentControlSet\Control\SafeBoot\Network"

                        def regfil(name):
                            try:
                                m = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, pathreg + name)
                                winreg.CloseKey(m)
                            except Exception as e:
                                c = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, pathreg + name)
                                registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, pathreg + name, 0,
                                                                         winreg.KEY_WRITE)
                                winreg.SetValueEx(registry_key, '(Default)', 0, winreg.REG_SZ, 'Service')
                                winreg.CloseKey(registry_key)
                        def Nregfil(name):
                            try:
                                m = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path2reg + name)
                                winreg.CloseKey(m)
                            except Exception as e:
                                c = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, path2reg + name)
                                registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path2reg + name, 0,
                                                                         winreg.KEY_WRITE)
                                winreg.SetValueEx(registry_key, '(Default)', 0, winreg.REG_SZ, 'Service')
                                winreg.CloseKey(registry_key)

                        regfil('\esfahanoud1')
                        regfil('\esfahanoud2')
                        regfil('\Wwinfilteroud')
                        Nregfil('\esfahanoud1')
                        Nregfil('\esfahanoud2')
                        Nregfil('\Wwinfilteroud')
                    if mmm == False:
                        break
                except:
                    pass

            #os.remove(dst1)
            #os.remove(dst2)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(AppServerSvc3)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(AppServerSvc3)
