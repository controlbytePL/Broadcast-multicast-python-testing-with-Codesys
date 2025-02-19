import socket
import struct

# Ustawienia multicastu
MULTICAST_GROUP = '239.0.0.1'  # Twój adres multicast
PORT = 50000                    # Port, na którym odbierasz dane

# Tworzymy gniazdo UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

# Umożliwia ponowne użycie adresu (nie blokuje portu)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Wiązanie do portu multicast
sock.bind(('', PORT))  # Odbiera z dowolnego interfejsu

# Dołączanie do grupy multicast
mreq = struct.pack("4sL", socket.inet_aton(MULTICAST_GROUP), socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

print(f"Nasłuchuję na {MULTICAST_GROUP}:{PORT}...")

# Odbieranie danych
while True:
    data, addr = sock.recvfrom(1024)  # Odbiór do 1024 bajtów
    print(f"Otrzymano od {addr}: {data.decode()}")