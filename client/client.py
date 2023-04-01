import socket
import tkinter as tk
import tkinter.messagebox
import entrance_ui as ui1
import main_ui as ui2

#global variables
BUFSIZE = 1024 * 4
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
root = tk.Tk()
root.geometry("880x600") #1000 la nguyen ban
root.configure(bg = "#FFFFFF")
root.title('Client')
root.resizable(False, False)

f1 = ui1.Entrance_UI(root)

def back(ui):
    ui.place_forget()
    f2.place(x = 0, y = 0)
    client.sendall(bytes("QUIT", "utf8"))

def disconnect():
    f2.place_forget()
    f1.place(x = 0, y = 0)
    client.sendall(bytes("QUIT", "utf8"))
    return

def show_main_ui():
    f1.place_forget()
    global f2
    f2 = ui2.Main_UI(root)
    # f2.button_1.configure(command = live_screen)
    # f2.button_2.configure(command = registry)
    # f2.button_3.configure(command = mac_address)
    # f2.button_4.configure(command = directory_tree)
    # f2.button_5.configure(command = app_process)
    # f2.button_6.configure(command = disconnect)
    # f2.button_7.configure(command = keylogger)
    # f2.button_8.configure(command = shutdown_logout)
    return


def connect():
    global client
    ip = f1.input.get()
    try:
        client.connect((ip, 5656))
        tk.messagebox.showinfo(message = "Connect successfully!")
        show_main_ui()
    except:
        tk.messagebox.showerror(message = "Cannot connect!")       
    return
show_main_ui()
#f1.button_connect.configure(command = connect)
root.mainloop()