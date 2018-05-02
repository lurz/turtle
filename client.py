#!/usr/bin/env python

import asyncio
import websockets

@asyncio.coroutine
def main():
    server_ip = input("server ip: ")
    port = input("server port: ")
    server_ip = "localhost"
    port = "8080"
    host = "ws://{}:".format(server_ip) + port
    print ("start up client server")
    websocket = yield from websockets.connect(host)

    while (True):
        name = input("What's your name? ")
        yield from websocket.send(name)
        print("> {}".format(name))

        greeting = yield from websocket.recv()
        print("< {}".format(greeting))

asyncio.get_event_loop().run_until_complete(main())
#asyncio.get_event_loop().run_forever()