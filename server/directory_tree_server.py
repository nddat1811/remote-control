import  pickle
import os

BUFSIZE = 1024 * 4
SEPARATOR = "<SEPARATOR>"

def show_tree(sock):
    listD = []
    for c in range(ord('A'), ord('Z') + 1):
        path = chr(c) + ":\\"
        if os.path.isdir(path):
            listD.append(path)
    data = pickle.dumps(listD)
    sock.sendall(str(len(data)).encode())
    temp = sock.recv(BUFSIZE)
    sock.sendall(data)

def send_list_dirs(sock):
    path = sock.recv(BUFSIZE).decode()
    if not os.path.isdir(path):
        return [False, path]

    try:
        listT = []
        listD = os.listdir(path)
        for d in listD:
            listT.append((d, os.path.isdir(path + "\\" + d)))
        
        data = pickle.dumps(listT)
        sock.sendall(str(len(data)).encode())
        temp = sock.recv(BUFSIZE)
        sock.sendall(data)
        return [True, path]
    except:
        sock.sendall("error".encode())
        return [False, "error"]    

def delete_file(sock):
    p = sock.recv(BUFSIZE).decode()
    if os.path.exists(p):
        try:
            os.remove(p)
            sock.sendall("ok".encode())
        except:
            sock.sendall("error".encode())
            return
    else:
        sock.sendall("error".encode())
        return

# copy file from client to server
def copy_file_to_server(sock):
    received = sock.recv(BUFSIZE).decode()
    if (received == "-1"):
        sock.sendall("-1".encode())
        return
    filename, filesize, path = received.split(SEPARATOR)
    filename = os.path.basename(filename)
    filesize = int(filesize)
    sock.sendall("received filename".encode())
    data = b""
    while len(data) < filesize:
        packet = sock.recv(999999)
        data += packet
    if (data == "-1"):
        sock.sendall("-1".encode())
        return
    try:
        with open(path + filename, "wb") as f:
            f.write(data)
        sock.sendall("received content".encode())
    except:
        sock.sendall("-1".encode())

# copy file from server to client
def copyFileToClient(sock):
    filename = sock.recv(BUFSIZE).decode()
    if filename == "-1" or not os.path.isfile(filename):
        sock.sendall("-1".encode())
        return
    filesize = os.path.getsize(filename)
    sock.sendall(str(filesize).encode())
    temp = sock.recv(BUFSIZE)
    with open(filename, "rb") as f:
        data = f.read()
        sock.sendall(data)

def directory(client):
    isMod = False
    
    while True:
        if not isMod:
            mod = client.recv(BUFSIZE).decode()

        if (mod == "SHOW"):
            show_tree(client)
            while True:
                check = send_list_dirs(client)
                if not check[0]:    
                    mod = check[1]
                    if (mod != "error"):
                        isMod = True
                        break
        
        # copy file from client to server
        elif (mod == "COPYTO"):
            client.sendall("OK".encode())
            copy_file_to_server(client)
            isMod = False

        # copy file from server to client
        elif (mod == "COPY"):
            client.sendall("OK".encode())
            copyFileToClient(client)
            isMod = False

        elif (mod == "DEL"):
            client.sendall("OK".encode())
            delete_file(client)
            isMod = False

        elif (mod == "QUIT"):
            return
        
        else:
            client.sendall("-1".encode())