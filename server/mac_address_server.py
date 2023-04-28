import uuid
def mac_address(client):
    mac = hex(uuid.getnode())
    client.sendall(bytes(mac, "utf8"))
    return