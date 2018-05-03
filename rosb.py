#!/usr/bin/env python
import json
from websocket import create_connection
import threading
import time

def receivemsg(ws):
    while True:
        back = ""
        back = json.loads(ws.recv())
        print(back)
        time.sleep(1)

def main():
    ws = create_connection("ws://192.168.86.51:9090")
    t = threading.Thread(target=receivemsg, args=(ws,))
    t.start()
    while (True):
        sendmsg = input("Send command: ")
        if sendmsg == "exit":
            ws.close()
            break
        if sendmsg == "hello":
            msg = {}
            msg["op"] = "publish"
            msg["topic"] = "hello"
            msg["msg"] = {"data":"hello"}
            msg = json.dumps(msg)
            ws.send(msg)
        if sendmsg == "adver":
            msg = { "op": "advertise", "topic": "hello", "type": "std_msgs/String"}
            ws.send(json.dumps(msg))
        if sendmsg == "subs":
            msg = {"op": "subscribe", "topic": "/hello"}
            ws.send(json.dumps(msg))
        if sendmsg == "w":
            lo = {"linear": {"x": 0.2}, "angular": {"z": 0}}
            msg = {"op": "publish", "topic": "/cmd_vel_mux/input/navi", "type": "geometry_msgs/Twist", "msg": lo}
            ws.send(json.dumps(msg))
        if sendmsg == "s":
            lo = {"linear": {"x": -0.2}, "angular": {"z": 0}}
            msg = {"op": "publish", "topic": "/cmd_vel_mux/input/navi", "type": "geometry_msgs/Twist", "msg": lo}
            ws.send(json.dumps(msg))
        if sendmsg == "a":
            lo = {"linear": {"x": 0}, "angular": {"z": 1}}
            msg = {"op": "publish", "topic": "/cmd_vel_mux/input/navi", "type": "geometry_msgs/Twist", "msg": lo}
            ws.send(json.dumps(msg))
        if sendmsg == "d":
            lo = {"linear": {"x": 0}, "angular": {"z": -1}}
            msg = {"op": "publish", "topic": "/cmd_vel_mux/input/navi", "type": "geometry_msgs/Twist", "msg": lo}
            ws.send(json.dumps(msg))
        if sendmsg == "k":
            lo = {"linear": {"x": 0}, "angular": {"z": 0}}
            msg = {"op": "publish", "topic": "/cmd_vel_mux/input/navi", "type": "geometry_msgs/Twist", "msg": lo}
            ws.send(json.dumps(msg))
        print ("Command done with no msg back")

if __name__ == '__main__':
    main()

    