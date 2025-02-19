import socket
import struct

# Multicast settings
MULTICAST_GROUP = '239.0.0.1'  # Your multicast address
PORT = 50000                    # Port on which to receive data

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

# Allow reuse of the address (prevents port blocking)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind to the multicast port
sock.bind(('', PORT))  # Receive from any network interface

# Join the multicast group
mreq = struct.pack("4sL", socket.inet_aton(MULTICAST_GROUP), socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

print(f"Listening on {MULTICAST_GROUP}:{PORT}...")

# Receiving data
while True:
    data, addr = sock.recvfrom(1024)  # Receive up to 1024 bytes
    print(f"Received from {addr}: {data.decode()}")
