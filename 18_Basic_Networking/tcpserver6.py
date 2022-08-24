from concurrent import futures as cf
import socket

IP_ADDR = 'localhost'
IP_PORT = 8881

def handle(new_sock, address):
    print('Connected from', address)
    with new_sock:
        while True:
            received = new_sock.recv(1024)
            if not received:
                break
            s = received.decode('utf-8', errors='replace')
            print(f'Recv: {s!r}')
            new_sock.sendall(received)
            print(f'Echo: {s!r}')
    print(f'Disconnected from {address}')


with socket.socket(socket.AF_INET6,    # IPv6
                   socket.SOCK_STREAM  # TCP
                   ) as servsock:
    servsock.bind((IP_ADDR, IP_PORT))
    servsock.listen(5)
    print(f'Serving at {servsock.getsockname()}')
    with cf.ThreadPoolExecutor(20) as e:
        while True:
            new_sock, address = servsock.accept()
            e.submit(handle, new_sock, address)
