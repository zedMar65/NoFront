import socket
import hashlib
import time
class Compiler:
    def __init__(self):
        pass

    @staticmethod
    def run(file, flags):
        if flags:
            print("Running", file, "with flags", flags)
            return "ASDASDASDASDASDASDASD"
        else:
            print("Running", file)
            return "ASDASDASDASDASDASDASD"
    @staticmethod
    def compile(file):
        print("Compiling", file)
        # later
    @staticmethod
    def connect(ip, password="", port=1598):
        try:
            passwordHash = hashlib.sha256(password.encode()).digest()
            client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            client.sendto(f"CON{ip}".encode(), (ip, port))
            client.sendto(str(passwordHash).encode(), (ip, port))
            data, addresss = client.recvfrom(1024)
            if addresss[0] == ip:
                if data.decode() == "CON":
                    return [1, ip, password, port]
                else:
                    return [0]
        except Exception as e:
            print(e)
            return [0]
    @staticmethod
    def acceptConnection(socketC, ip, password="", port=1598, timeout=5):
        passwordHash = hashlib.sha256(password.encode()).digest()
        startTime= time.time()
        while startTime + timeout > time.time():
            data, addr = socketC.recvfrom(1024)
            if addr[0] == ip:
                if data.decode() == str(passwordHash):
                    socketC.sendto("CON".encode(), addr)
                    return [1, addr[0], password, port]
                else:
                    return [0]
            else:
                pass
        return [0]
    @staticmethod
    def listen(port=1598):
        try:
            server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            server.bind(("", port))
            data, addr = server.recvfrom(1024)
            if data:
                return data.decode(), addr[0], server
            else:
                return None
        except:
            return None