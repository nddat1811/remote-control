import os
import gmail as g

BUFSIZE = 1024 * 4
SEPARATOR = "<SEPARATOR>"

def show_tree():
    listD = []
    for c in range(ord('A'), ord('Z') + 1):
        path = chr(c) + ":\\"
        if os.path.isdir(path):
            listD.append(path)
    g.send_mail("SHOWTREE", listD)

def send_list_dirs():
    letter = g.read_mail()
    path = ""
    if "PATH" in letter:
        path = letter.split("PATH:")[1]
    elif letter == "no":
        return [True, ""]
    if not os.path.isdir(path):
        path = letter
        return [False, path]
    try:
        listT = []
        listD = os.listdir(path)
        for d in listD:
            listT.append((d, os.path.isdir(path + "\\" + d)))
        g.send_mail("LIST_DIR", listT)
        return [True, path]
    except:
        g.send_mail("error", "err")
        return [False, "error"]    

def delete_file():
    while True:
        letter = g.read_mail()
        if "DELFILE" in letter:
            p = letter.split("DELFILE:")[1]
            if os.path.exists(p):
                try:
                    os.remove(p)
                    g.send_mail("DELFILE", "SUCCESS")
                    return
                except:
                    g.send_mail("DELFILE", "error")
                    return
            else:
                g.send_mail("DELFILE", "error")
                return

# copy file from client to server
def copy_file_to_server():
    while True:

        received = g.read_mail()
        if "FILE_PATH" in received:
            path = received.split("FILE_PATH:")[1]
            g.send_mail("FILE_PATH", "OK")
            path = os.path.normpath(path)
            # path = r'{path}'
            while True:
                letter = g.get_mail_with_attachment(path)
                if "FILECLIENT" in letter:
                    g.send_mail("RECEIVED", "OK")
                    return
                elif "ERROR" in letter:
                    return
        elif "NOTFILE" in received:
            return

# copy file from server to client
def copy_file_to_client():
    while True:
        letter = g.read_mail()
        if "FILENAME" in letter:
            filename = letter.split("FILENAME:")[1]
            if filename == "-1" or not os.path.isfile(filename):
                g.send_mail("FILE_TO_CLIENT", "NOTOK")
                return
            cmd = 'FILEDATA'
            g.send_mail_with_attachment(cmd, filename)
            return
        elif "NOTFILE" in letter:
            return

def directory():
    isMod = False
    
    while True:
        if not isMod:
            mod = g.read_mail()
        
        if (mod == "SHOW"):
            show_tree()
            while True:
                check = send_list_dirs()
                if not check[0]:    
                    mod = check[1]
                    if (mod != "error"):
                        isMod = True
                        break
        
        # copy file from client to server
        elif (mod == "COPYTO"):
            g.send_mail("COPYTO","OK")
            copy_file_to_server()
            isMod = False

        # copy file from server to client
        elif (mod == "COPY"):
            g.send_mail("COPY","OK")
            copy_file_to_client()
            isMod = False

        elif "XOAFILE" in mod:
            g.send_mail("DEL","OK")
            delete_file()
            isMod = False

        elif (mod == "QUIT"):
            return
        