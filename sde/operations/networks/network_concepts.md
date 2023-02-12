# Networks

## ARP

* `ARP`: Address Resolution Protocol
* Operates at `Layer 2`.
* Tries to identify the `destination` IP, from a `Layer 2` [`broadcast frame`](network_concepts.md#broadcast-frame).
  * > Who has IP address 10.1.1.100?
* Every device stores a table of MAC addresses it discovers in its network.
  * A server device will store the IPv4 addresses associated to the discovered MAC addresses.
  * A switch device will map the MAC addresses of connected devices to its corresponding switch ports.
* To see the MAC addresses stored in a server device run:

  Command:

  ```cmd
  arp -a
  ```

  output:

  ```cmd
  Internet Address  Physical Address  Type
  10.1.12           0006.2abe.7da4    dynamic
  ```

* To see the MAC addresses stored in a (Cisco) switch run:

  Command:

  ```ios cli
  mac address-table
  ```

  Output:

  ```ios cli
  Vlan  Mac Address     Type    Ports
  ----  -----------     ----    -----
  1     0004.9add.c016  DYNAMIC Gig1/0/1
  1     0006.2abe.7da4  DYNAMIC Gig1/0/2
  ```

## Broadcast Frame

* A message with a real `source` IP address, but with a dummy `destination` IP address, composed of all `F`:
  * `FFFF.FFFF.FFFF`

## PDU

* `PDU`: Protocol Data Unit
  * Contains the message's data.

## Protocol Numbers

* [Protocol Numbers (IANA)](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml)

Common Protocol Numbers:  

| Decimal | Keyword | Protocol |
| ------- | ------- | -------- |
| 4 | IPv4 | IPv4 encapsulation|
| 6  | TCP | Transmission Control |
| 17 |  UDP | User Datagram |
| 41 |  IPv6 | IPv6 encapsulation |

## Port Number Registry

* [Service Name and Transport Protocol Port Number Registry (IANA)](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml)

Common Port Numbers:

| Service Name | Port Number | Description |
| ------------ | ----------- | ----------- |
| ftp | 21 | File Transfer Protocol |
| ssh | 22 | Secure Shell Protocol |
| sftp* | 22 | SSH File Transfer Protocol |
| telnet | 23 | Telnet |
| smtp | 25 | Simple Mail Transfer |
| domain | 53 | Domain Name Server (DNS) |
| tftp | 69 | Trivial File Transfer |
| http | 80 | Hypertext Transfer Protocol |
| www | 80 | World Wide Web |
| sftp* | 115 | Simple File Transfer Protocol |
| https | 443 | HTTP Protocol over TLS/SSL |

## Ephemeral/Dynamic Port

* [Definition: Wikipedia](https://en.wikipedia.org/wiki/Ephemeral_port)
  * > An ephemeral port is a communications endpoint (port) of a transport layer protocol of the Internet protocol suite that is used for only a short period of time for the duration of a communication session.
  * > Such short-lived ports are allocated automatically within a predefined range of port numbers by the IP stack software of a computer operating system.
* Ephemeral Port Ranges:
  * > Port numbers are assigned in various ways, based on three ranges:
    * > System Ports (0-1023),
    * > User Ports (1024-49151), and
    * > Dynamic and/or Private Ports (49152-65535);
  * > The different uses of these ranges are described in [RFC6335](https://www.rfc-editor.org/rfc/rfc6335.html).
    * Source: [IANA](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml?search=telnet)
  * > The RFC 6056 says that the range for ephemeral ports should be 1024–65535.
    * Source: [Wikipedia](https://en.wikipedia.org/wiki/Ephemeral_port#Range)
* When a client initiates a session to a well-known port (e.g. 80) on a server (i.e. the `DESTINATION PORT:{integer}` in the [PDU](network_concepts.md#pdu)'s `Layer 4` section), it'll use an ephemeral port number by default for the `SOURCE PORT:{integer}` field.
* When the server responds, the `DESTINATION PORT:{integer}` and `SOURCE PORT:{integer}` fields are reversed, so the response returns to the same port from were the request was sent.

## How do layers know what protocol to use?

* When a device receives a frame at `Layer 2`, it needs to know which protocol to use for the message's higher layer protocol.
* For example:
  * With `Ethernet II` in the `Layer 2` section of the [`PDU`](network_concepts.md#pdu), the field `TYPE:{Hexadecimal}` contains a hexadecimal value representing the protocol to use for interpreting the frame's data in its next layer (i.e. `Layer 3`), e.g.:
    * `TYPE:0x0800` for using IPv4 protocol in `Layer 3`.
  * With `IP` in the `Layer 3` section of the [`PDU`](network_concepts.md#pdu), the field is `PRO:{hexadecimal}` for the protocol to be used in its next layer (i.e. `Layer 4`), e.g.:
    * `PRO:0x06` for using `TCP` protocol in `Layer 4`.
  * With `TCP` in the `Layer 4` section of the [`PDU`](network_concepts.md#pdu), the field `DESTINATION PORT:{integer}` contains a decimal value representing the the protocol for `Layer 7`, e.g.:
    * `DESTINATION PORT: 80` for using `HTTP` in `Layer 7`.

## Why are services mapped to specific port numbers?

* So the data sent over the network is routed to its appropriate application.
* For example:
  * Data sent for interacting with an email application, needs to be routed to the specific port where the email application is listening to for incoming data.
  * There can be multiple protocols for handling a specific type of application, eg.:
    * `smtp`: 25
    * `pop3`: 110
    * `imap`: 143

## Octet

* > The octet is a unit of digital information in computing and telecommunications that consists of eight bits.
* > The term is often used when the term byte might be ambiguous, as the byte has historically been used for storage units of a variety of sizes.
  * Source: [Wikipedia](https://en.wikipedia.org/wiki/Octet_(computing))
* In computer and network technology, an octet represents an 8-bit quantity.
* An octet is always eight bits.

## IPv4 Addresses

* It is a `Layer 3` address asigned by an administrator.
* It is used to uniquely identify a device on an IP network.
* Every device on the internet has a unique IP address.
* IPv4 is a "Connectionless Protocol":
  * There are no sessions formed when traffic is transmitted.
  * The transmitter simply sends data without notification to the receiver.
  * No status information is sent back from the receiver to the transmitter.
  * For a connectione oriented protocol, there is TCP.
* Packets are treated independently of ther packets.
  * Hence different packages may take different paths to get to its destination, as routers can make a routing decision based on:
    * Load balancing
    * Bandwidth (OSPF)
    * Hopcount (RIP)
* IPv4 offers "best effort delivery" of packet.
  * There is no guarantee of packet delivery.
  * It could be:
    * Misdirected
    * Duplicated
    * Lost in transmission
  * No data recovery reatures:
    * If packet gets corrupted in traffic, the end devices need to handle that.

### IPv4 Format Overview

* An IPv4 address consists of 4 octets, i.e. it has 32 bits.
* The decimal value in each octet is in the range 0 to 255.
* e.g.:
  * Decimal: 10.129.16.123
  * Binary: 00001010.10000001.0001000.01111011

## Network Address Portion

* AKA, `Network ID`
* Identifies a specific network.

## Host Address Portion

* AKA, `Host ID`
* Identify a specific endpoint on a network.
  * e.g. server, printers, PCs, smartphones, tablets, etc.

## IPv6 Addresses

* Introduced because of IPv4 address exhaustion.

## Private Addresses

* Formalised via RFC-1918.
* 3 blocks of IP address space reserved for private internets:
  * `10.0.0.0` - `10.255.255.255` (10/8 prefix)
  * `172.16.0.0` - `172.31.255.255` (172.16/12 prefix)
  * `182.168.0.0` - `192.168.255.255` (192.168/16 prefix)

## Public vs Private Addresses

* Get the IP Address of a domain name -> `nslookup`

  Command:

  ```bash
  nslookup www.google.com
  ```

  Output:

  ```bash
  Server:         172.28.48.1
  Address:        172.28.48.1#53

  Non-authoritative answer:
  Name:   www.google.com
  Address: 142.250.200.4
  Name:   www.google.com
  Address: 2a00:1450:4009:822::2004
  ```

## Address Classes

* Address classes were used between 1981 and 1993, when classless domain routing was introduced in 1993.
* They divided IPv4 addresses into 5 classes:
  * Unicast Traffic:
    * When one device talks to another single device.
    * Class A
    * Class B
    * Class C
  * Multicast Traffic:
    * When one device talks to multiple devices.
    * Class D
  * Reserved Addresses:
    * Reserved for future or experimental purposes.
    * Class E
* In IPv4, address classes has been replaced with CIDR.
* IPv6 does not use address classes.

### Class A

* Starts with a binary `0`.
* Binary range: `0.0.0.0` - `127.255.255.255`
  * i.e. `00000000.00000000.00000000.00000000` - `0111111.11111111.11111111.11111111`
* Exceptions:
  * `127.0.0.1` is reserved for loopback.
  * `0.1.1.1` is reserved for default network.
* Actual range: `1.0.0.0` - `126.255.255.255`
* Network Address Portion:
  * 1st octet
* Host Address Portion:
  * 2nd octet
  * 3rd octet
  * 4th octet

### Class B

* Starts with binary `10`.
* Binary range: `128.0.0.0` - `191.255.255.255`
  * i.e. `10000000.00000000.00000000.00000000` - `10111111.11111111.11111111.11111111`
* Network Address Portion:
  * 1st octet
  * 2nd octet
* Host Address Portion:
  * 3rd octet
  * 4th octet

### Class C
  
* Starts with binary `110`.
* Binary range: `192.0.0.0` - `223.255.255.255`
  * i.e. `11000000.00000000.00000000.00000000` - `11011111.11111111.11111111.11111111`
* Network Address Portion:
  * 1st octet
  * 2nd octet
  * 3rd octet
* Host Address Portion:
  * 4th octet

### Class D

* Starts with binary `1110`.
* Binary range: `224.0.0.0` - `239.255.255.255`
  * i.e. `11100000.00000000.00000000.00000000` - `11101111.11111111.11111111.11111111`

### Class E

* Starts with binary `1111`.
* Binary range: `240.0.0.0` - `255.255.255.255`
  * i.e. `11110000.00000000.00000000.00000000` - `11111111.11111111.11111111.11111111`

## Special Addresses

### Directed Broadcast Address

* Used by the host to send data to all devices on a specific network.
* Binary `1`s in the entire host portion of the address.
* e.g.:
  * In a network `172.31.0.0` (i.e. Class B)
  * Directed Broadcast: `172.31.255.255`
* Routers can route Directed Broadcasts, but are **disabled by default** to avoid hacks.
  * There are hacking utilities that can be downloaded, e.g. `smurf`.
  * Used for Denial of Service Attacks.
  * Every host on the same network would:
    * Receive the broadcast.
    * Accept the broadcast.
    * Forwards it to higher level protocol for processing.
  * All of the above actions consume CPU resources on the host.
  * Every host on the network that received the directed broadcast would return a response to the sender device (source address).
  * This avalanche of responses to the source address would cause the Denial of Service on the sender device.
  * A hacker would send the directed broadcast from a different device than the target device, but on the same network, and point the source address to the target device.

### Local Loopback Address

* Used to let a system send a message to itself.
  * This is useful to make sure that the TCP/IP stack is correctly installed on a machine. #DOUBT
* Any IP address on the 127.X.X.X network is a Local Loopback Address.
  * Normally used: `127.0.0.1`
  * However, it's a Class A address, hence ~16 million IPv4 addresses were wasted with this setup.
* In IPv6, the Local Loopback Address is `::1` (this way no addresses are wasted as in IPv4).
* NB: Routers and switches also have loopback addresses, which are not the same as _local_ loopback addresses.

## Local Broadcast Address

* Used to communicate with all devices on a local network.
* The address is all binary `1`s, i.e.:
  * `11111111.11111111.11111111.11111111`
  * `255.255.255.255`
* It is used for:
  * When a host requests an IP address from a DHCP server (because it hasn't been assigned one yet), i.e.
    * A new device boots up (or connects to a wifi router) and sends a broadcast via the Local Broadcast Address.
    * The DHCP server hears that broadcast.
    * The DHCP server then allocates an IP address to the host from a pool or scope of IP addresses.
* It is always dropped by `Layer 3` devices such as routers and `Layer 3` switches.
  * So two devices on different networks can't communicate over Local Broadcast Address because the router or switch will not relay the broadcast.
  * You can override such functionality by enabling `IP forwarding` AKA `DHCP forwarding` AKA `DHCP relay`, so your router or switch can forward the broadcast to the DHCP server on the other local network.
    * Technically, the broadcast on the Local Broadcast Address would be dropped by the router/switch, but it would send a unicast DHCP request to the DHCP server on behalf of the sender device.
    * This would allow the router/switch to proxy the DHCP request on behalf of the sender device.

## Network Masks

## CIDR

## DHCP Server

* DHCP: Dynamic Host Configuration Protocol
* Provides IP addresses dynamically to devices such as PCs, smart phones, tablets, ip telephones, etc.
* Enables users to not have to manually assign an IP address to every device on his network.

## RFC

* RFC: Request for Comments
* RFC1149

## Binary Conversion Table

| Octat Bit  | 2^7 | 2^6 | 2^5 | 2^4 | 2^3 | 2^2 | 2^1 | 2^0 |
| ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
| Binary     |  1  |  1  |  1  |  1  |  1  |  1  |  1  |  1  |
| Decimal    | 128 |  64 |  32 |  16 |  8  |  4  |  2  |  1  |

## Binary Conversion Calculator

Find code [here](binary_calculator.py).

## Hexadecimal

* A hexadecimal value is base 16.
  * Value ranges from 0 to f.
* A hex value is 4 bits (`ff{hex}` == `15{dec}` == `1111{bin}`)

## MAC Addresses

* It is a `Layer 2` address built into the [NIC](network_concepts.md#nic)
* A MAC address (aka physical address) is composed of 12 hexadecimal values, grouped in 3 sets of 4.
  * The first 6 hex values represent the hardware vendor code, and the remaining 6 hex values represent unique identifier for the MAC address.
* A MAC address is 48 bits long.
  * i.e. 16 hex values, each of 4 bits.

## NIC

* `NIC`: Network Interface Card
  * AKA: Network Interface Controller

## Router

* Routes traffic to a destination IP address based on a hierarchical addressing structure:
  * IPv4 and IPv6 addresses have a [network address portion](network_concepts.md#network-address-portion) and a [host address portion](network_concepts.md#host-address-portion).
* Routers don't route traffic to an IP Address, but by using only the [network address portion](network_concepts.md#network-address-portion) of an IP address.
* Routers maintain routing tables that contain network addresses.
* Routers look at the destination IP address in a packet and match that to a network address in their routing table.

## TCP

* TCP: Transmision Control Protocol
* TCP will set up a session before transmiting data, via the Three-Way Handshake.
* Three-Way Handshake:
  * The transmitter sends a `SYN` (or synchronization message) to the receiver.
  * The receiver sends a `SYN Ack` (or synchronization acknowledgement message) to the transmitter.
  * The transmitter sends an `Ack` (or acknowledgement message) to the receiver.

## UDP

* UDP: User Datagram Protocol
