# Networks

## ARC

* `ARC`: Address Resolution Protocol
* Operates at `Layer 2`.
* Tries to identify the `destination` IP, from a `Layer 2` [`broadcast frame`](network_concepts.md#broadcast-frame).
  * > Who has IP address 10.1.1.100?

## Broadcast Frame

* A message with a real `source` IP address, but with a dummy `destination` address, composed of all `F`:
  * `FFFF.FFFF.FFFF`

## PDU

* `PDU`: Protocol Data Unit
  * Contains the message's data.

## Protocol Numbres (IANA)

* [Protocol Numbers](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml)

## Ephemeral/dynamic Port

* xxx

## How do layers know what protocol to use?

* When a device receives a frame at `Layer 2`, it needs to know which protocol to use for the message's higher layer protocol.
* For example:
  * With `Ethernet II` in the `Layer 2` section of the [`PDU`](network_concepts.md#pdu), the field `TYPE:{Hexadecimal}` contains a hexadecimal value representing the protocol to use for interpreting the frame's data in its next layer (i.e. `Layer 3`), e.g.:
    * `TYPE:0x0800` for using IPv4 protocol in `Layer 3`.
  * With `IP` in the `Layer 3` section of the [`PDU`](network_concepts.md#pdu), the field is `PRO:{hexadecimal}` for the protocol to be used in its next layer (i.e. `Layer 4`), e.g.:
    * `PRO:0x06` for using `TCP` protocol in `Layer 4`.
  
