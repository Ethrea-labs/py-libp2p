# from multiaddr import (
#     Multiaddr,
# )
# import trio

# from libp2p.transport.quic.transport import (
#     QuicTransport,
# )


# async def main():
#     async def handler(protocol) -> None:
#         while True:
#             continue

#     transport1 = QuicTransport(host="127.0.0.1", port=0)
#     transport2 = QuicTransport(host="127.0.0.1", port=0)

#     async with trio.open_nursery() as nursery:
#         listener = transport1.create_listener(handler)
#         await listener.listen(Multiaddr("/ip4/127.0.0.1/udp/0/quic"), nursery)

#         conn = await transport2.dial(listener.get_addrs()[0])
#         assert conn is not None


# if __name__ == "__main__":
#     trio.run(main)
