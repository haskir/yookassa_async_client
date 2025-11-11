from socket import AF_INET, SOCK_STREAM
from socket import socket as Socket

host: str = "localhost"
port: int = 8888


def send(message: str, _socket: Socket) -> None:
    encoded: bytes = message.encode()
    length: bytes = bytes(len(encoded))
    _socket.send(length)
    _socket.send(encoded)
    print(f"Sent: {message}")


def recieve(_socket: Socket) -> str | None:
    try:
        # length: int = int(_socket.recv(1024))
        length: int = 1024
        recieved: bytes = _socket.recv(length)
        print(f"Recived: {recieved}")
        return recieved.decode().strip()
    except Exception as e:
        print(f"Error: {repr(e)}")
        return None


def main():
    sock: Socket = Socket(AF_INET, SOCK_STREAM)
    sock.connect((host, port))
    while True:
        try:
            send(input("Сообщение:\n") or "EMPTY", sock)
            recieve(sock)
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()