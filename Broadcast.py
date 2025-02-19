import socket

# UDP settings
UDP_IP = "0.0.0.0"  # Listen on all available network interfaces
UDP_PORT = 50000     # Port matching your CODESYS broadcast

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.bind((UDP_IP, UDP_PORT))

print(f"Listening for UDP broadcast on port {UDP_PORT}...\n")

while True:
    data, addr = sock.recvfrom(1024)  # Buffer size is 1024 bytes
    print(f"Received message from {addr[0]} ({addr[1]}): {data.decode('utf-8')}")
