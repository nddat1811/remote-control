import uuid
def mac_address(client):
    mac = hex(uuid.getnode())
    print("mac ne: ", mac)
    client.sendall(bytes(mac, "utf8"))
    return