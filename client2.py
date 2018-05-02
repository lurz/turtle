#!/usr/bin/env python

from websocket import create_connection

while (True):
    ws = create_connection("ws://192.168.86.51:8080")
    sendmsg = input("Send command: ")
    if sendmsg == "exit":
        ws.close()
        break
    ws.send(sendmsg)
    result = ws.recv()
    print ("Command done " + str(result))
    