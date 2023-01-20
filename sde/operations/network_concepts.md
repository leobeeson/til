# Networks

## ARC

* `ARC`: Address Resolution Protocol
* Operates at `Layer 2`.
* Tries to identify the `destination` IP, from a `Layer 2` [`broadcast frame`](network_concepts.md#broadcast-frame).
  * > Who has IP address 10.1.1.100?

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
| 4	| IPv4	| IPv4 encapsulation| 
| 6	 | TCP |	Transmission Control |
| 17 | 	UDP |	User Datagram |
| 41 | 	IPv6 |	IPv6 encapsulation |

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
| tftp	| 69	| Trivial File Transfer |
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

## What are network octets?

* > The octet is a unit of digital information in computing and telecommunications that consists of eight bits.
* > The term is often used when the term byte might be ambiguous, as the byte has historically been used for storage units of a variety of sizes.
  * Source: [Wikipedia](https://en.wikipedia.org/wiki/Octet_(computing))
* In computer and network technology, an octet represents an 8-bit quantity.
* An octet is always eight bits.

## IPv4 Addresses

* An address used to uniquely identify a device on an IP network.
* An IPv4 address consists of 4 octets, i.e. it has 32 bits.
* The decimal value in each octet is in the range 0 to 255.
* e.g.:
  * Decimal: 10.129.16.123
  * Binary: 00001010.10000001.0001000.01111011

## Binary Conversion Table

| Octate Bit | 2^7 | 2^6 | 2^5 | 2^4 | 2^3 | 2^2 | 2^1 | 2^0 |
| ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
| Binary     |  1  |  1  |  1  |  1  |  1  |  1  |  1  |  1  |
| Decimal    | 128 |  64 |  32 |  16 |  8  |  4  |  2  |  1  |
