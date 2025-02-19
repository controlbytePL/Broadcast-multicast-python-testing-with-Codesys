# UDP Broadcast and Multicast in Codesys

This repository contains a Codesys project demonstrating how to send UDP broadcast and multicast messages. The implementation uses `NBS.UDP_Peer` to transmit messages over a network.

## Features

- **Broadcast Communication**: Sends UDP packets to all devices in the network.
- **Multicast Communication**: Sends UDP packets to a specific group of devices.
- **Error Handling**: Implements basic error detection during transmission.
- **Testing Integration**: Compatible with Python scripts for testing.

## Project Structure

- **Multicast\_PRG**: Program handling multicast communication.
- **Broadcast\_UDP**: Program handling broadcast communication.
- **Task Configuration**: Defines execution cycles.

## Configuration

### Broadcast Setup

- Local IP: `127.0.0.1`
- Broadcast Address: `255.255.255.255`
- Port: `50000`

### Multicast Setup

- Local IP: `192.168.33.4` (your Ethernet card IP address)
- Multicast Address: `239.0.0.1` (multicast group)
- Port: `50000`

## Usage

1. Load the Codesys project.
2. Set up the correct IP configurations based on your network.
3. Run the project and monitor the messages using Wireshark.
4. Use the Python testing scripts from the linked repository for validation.

## Testing with Python

For testing UDP Broadcast and Multicast messages, you can use the Python scripts available in this repository:
[Python UDP Testing Scripts](https://github.com/controlbytePL/Broadcast-multicast-python-testing-with-Codesys)

## Wireshark Filter

To capture relevant UDP packets, use the following filter:

```plaintext
udp.dstport == 50000 && ip.dst == 255.255.255.255
```

## License

This project is open-source under the MIT License.

## Author

[ControlByte](https://github.com/controlbytePL)

