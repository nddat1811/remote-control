import socket
import tkinter as tk
import sys
import mac_address_server as mac
import shutdown_logout_server as sl

#Global variables
global client
BUFSIZE = 1024 * 4

def mac_address():
    global client
    mac.mac_address(client)
    return

def shutdown_logout():
    global client
    sl.shutdown_logout(client)
    return

def Connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = ''
    port = 5656
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))
    s.listen(100)
    global client
    client, addr = s.accept()
    while True:
        msg = client.recv(BUFSIZE).decode("utf8")
        if "QUIT" in msg:
            client.close()
            s.close()
            return
        elif "MAC" in msg:
            mac_address()
        # elif "KEYLOG" in msg:
        #     keylogger()
        
        # elif "LIVESCREEN" in msg:
        #     live_screen()
        # elif "APP_PRO" in msg:
        #     app_process()
        
        # elif "DIRECTORY" in msg:
        #     directory_tree()
        # elif "REGISTRY" in msg:
        #     registry()
        elif "SD_LO" in msg:
            shutdown_logout()
       
###############################################################################    



def create_window():
    # create Tk
    root = tk.Tk()
    # set window size
    root.geometry("200x200")
    # set name
    root.title("Server")
    # set background color #B4E4FF
    root['bg'] = '#B4E4FF'

    # create button OPEN
    tk.Button(root, text = "OPEN", width = 10, height = 2, fg = '#FFFFFF', bg = '#2B3467', 
        borderwidth=0, highlightthickness=0, command = Connect, relief="flat").place(x = 100, y = 100, anchor = "center")
    
    # Vòng lặp chạy chương trình
    root.mainloop()


create_window()




