import  psutil 
import os
import gmail as g


def list_apps():
    ls1 = list()
    ls2 = list()
    ls3 = list()

    cmd = 'powershell "gps | where {$_.mainWindowTitle} | select Description, ID, @{Name=\'ThreadCount\';Expression ={$_.Threads.Count}}'
    proc = os.popen(cmd).read().split('\n')
    tmp = list()
    for line in proc:
        if not line.isspace():
            tmp.append(line)
    tmp = tmp[3:]
    for line in tmp:
        try:
            arr = line.split(" ")
            if len(arr) < 3:
                continue
            if arr[0] == '' or arr[0] == ' ':
                continue

            name = arr[0]
            threads = arr[-1]
            ID = 0
            # interation
            cur = len(arr) - 2
            for i in range (cur, -1, -1):
                if len(arr[i]) != 0:
                    ID = arr[i]
                    cur = i
                    break
            for i in range (1, cur, 1):
                if len(arr[i]) != 0:
                    name += ' ' + arr[i]
            ls1.append(name)
            ls2.append(ID)
            ls3.append(threads)
        except:
            pass
    return ls1, ls2, ls3

def list_processes():
    ls1 = list()
    ls2 = list()
    ls3 = list()
    for proc in psutil.process_iter():
        try:
            # Get process name & pid from process object.
            name = proc.name()
            pid = proc.pid
            threads = proc.num_threads()
            ls1.append(str(name))
            ls2.append(str(pid))
            ls3.append(str(threads))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return ls1, ls2, ls3

def kill(pid):
    cmd = 'taskkill.exe /F /PID ' + pid
    try:
        a = os.system(cmd)
        if a == 0:
            return 1
        else:
            return 0
    except:
        return 0
    
def start(name):
    cmd = 'start ' + name
    try:
        a = os.system(cmd)
        if a == 0:
            return 1
        else:
            return 0
    except:
        return 0

def app_process():
    global msg
    while True:
        msg = g.read_mail()
        if "QUIT" in msg:
            return
        ls1 = list()
        ls2 = list()
        ls3 = list()
        res =""
        #xem process 
        if msg == "PROCESS":
            ls1, ls2, ls3 = list_apps()
            action = 1
        elif msg == "APPLICATION":
            ls1, ls2, ls3 = list_processes()
            action = 1
        elif "KILL" in msg:
            tmp = msg.split(":")
            pid = tmp[1]
            try:
                if kill(pid) == 1:
                    g.send_mail("KILL","SUCCESS")
                else:
                    g.send_mail("KILL","UN")
            except:
                g.send_mail("KILL","UN") 
        elif "START" in msg:
            tmp = msg.split(":")
            pname = tmp[1]
            try:
                if start(pname) == 1:
                    g.send_mail("START","SUCCESS")
                else:
                    g.send_mail("START","UN")
            except:
                g.send_mail("START","UN") 
        else:
            action = -1

        if action == 1:
            g.send_mail("ls1", ls1)
            g.send_mail("ls2", ls2)
            g.send_mail("ls3", ls3)