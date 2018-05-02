#!/usr/bin/env python

import asyncio
import websockets

@asyncio.coroutine
def hello(websocket, path):
    print ("Server Setup!")
    name = yield from websocket.recv()
    status = False
    if name == "a":
        status = doa()
    if name == "b":
        status = dob()
    
    if status:
        yield from websocket.send("succeed!")
    else:
        yield from websocket.send("failed!")


def doa():
    print("a")
    return True

def dob():
    print("b")
    return True

start_server = websockets.serve(hello, 'localhost', 8080)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()