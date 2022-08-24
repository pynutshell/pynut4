import socket

UDP_IP = 'localhost'
UDP_PORT = 8883

with socket.socket(socket.AF_INET6,   # IPv6
                   socket.SOCK_DGRAM  # UDP
                   ) as sock:
    sock.bind((UDP_IP, UDP_PORT))
    print(f'Serving UDP at {UDP_IP}:{UDP_PORT}')
    while True:
        data, sender_addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
        print(f'RCVD {data!r} ({len(data)}) from {sender_addr}')
        bytes_sent = sock.sendto(data, sender_addr)
        print(f'SENT {data!r} ({bytes_sent}/{len(data)}) to {sender_addr}')
