import os

BUFSIZE = 1024 * 4
def shutdown_logout(client):
    while(True):
        msg = client.recv(BUFSIZE).decode("utf8")
        if "SHUTDOWN" in msg:
            os.system('shutdown -s -t 15')
        elif "LOGOUT" in msg:
            os.system('shutdown -l')
        else:
            return
    return
    