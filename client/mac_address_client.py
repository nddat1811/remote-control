import tkinter as tk

BUFSIZE = 1024 * 4

def mac_address(client):
    res = client.recv(BUFSIZE).decode("utf8")
    res = res[2:].upper()
    res = ':'.join(res[i:i + 2] for i in range(0, len(res), 2))
    tk.messagebox.showinfo(title='MAC Address', message=res)