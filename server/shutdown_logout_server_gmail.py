import os
import gmail as g

def shutdown_logout():
    while True:
        msg = g.read_mail()
        if "SHUTDOWN" in msg:
            os.system('shutdown -s -t 15')
            return
        elif "LOGOUT" in msg:
            os.system('shutdown -l')
            return