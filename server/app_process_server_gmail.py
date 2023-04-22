import  pickle, psutil, struct
import os
import gmailread as g

BUFSIZE = 1024 * 4

def send_data(cmd, data):
    size = struct.pack('!I', len(data))
    data = size + data
    g.send_mail(cmd, data)
    return

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
    print("ls1:", ls1)
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
    cmd = 'taskkill.exe /F /PID ' + str(pid)
    try:
        a = os.system(cmd)
        if a == 0:
            return 1
        else:
            return 0
    except:
        return 0
    
def start(name):
    os.system(name)
    return

def app_process():
    global msg
    while True:
        msg = g.read_mail()
        if "QUIT" in msg and len(msg) < 20:
            return
        res = 0
        ls1 = list()
        ls2 = list()
        ls3 = list()
        
        if msg == "PROCESS":
            print("zo day:")
            ls1, ls2, ls3 = list_apps()
            action = 1
        elif msg == "APPLICATION":
            print("zo day22:")
            ls1, ls2, ls3 = list_processes()
            action = 1
        elif msg != "no": 
            action = int(msg)
        else:
            action = -1
        #0-kill
        if action == 0:
            pid = g.read_mail()
            pid = int(pid)
            try:
                res = kill(pid)
            except:
                res = 0
        #1-xem
        # elif action == 1:
        #     try:
        #         status = g.read_mail()
        #         if "PROCESS" in status:
        #             ls1, ls2, ls3 = list_apps()
        #         else:
        #             ls1, ls2, ls3 = list_processes()
        #         res = 1
        #     except:
        #         res = 0
        #2-xoa
        elif action == 2:
            res = 1
        #3 - start
        elif action == 3:
            pname = g.read_mail()
            try:
                start(pname)
                res = 1
            except:
                res = 0
        if action != 1 and action != 3 and action != -1:
            g.send_mail("kill|xoa: ", res)
            # client.sendall(bytes(str(res), "utf8"))
        #send list app/process
        if action == 1:
            #ls1 = pickle.dumps(ls1)
            #ls2 = pickle.dumps(ls2)
            #ls3 = pickle.dumps(ls3)
            g.send_mail("ls1", ls1)
            g.send_mail("ls2", ls2)
            g.send_mail("ls3", ls3)
            #send_data("ls1", ls1)   
            #send_data("ls2", ls2)
            #send_data("ls3", ls3)