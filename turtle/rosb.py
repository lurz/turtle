#!/usr/bin/env python
import json
from websocket import create_connection
import threading
import time
import sys

def receivemsg(websocket_c):
    while True:
        back = ""
        back = json.loads(websocket_c.recv())
        print(back)
        time.sleep(1)

def sendmsg(websocket_c, op_type, topic, ):


def main():
    if len(sys.argv) != 2:
        print ("NEED IP ADDR")
        return
    server_ip = "ws://" + str(sys.argv[1]) +":9090"
    websocket_c = create_connection(server_ip)

    rec_thread = threading.Thread(target=receivemsg, args=(websocket_c,))
    rec_thread.start()
    
    while True:
        send_command = input("Send command: ")
        if send_command == "exit":
            websocket_c.close()
            break
        if send_command == "hello":
            msg = {}
            msg["op"] = "publish"
            msg["topic"] = "hello"
            msg["msg"] = {"data":"hello"}
            msg = json.dumps(msg)
            websocket_c.send(msg)
        if send_command == "adver":
            msg = { "op": "advertise", "topic": "hello", "type": "std_msgs/String"}
            websocket_c.send(json.dumps(msg))
        if send_command == "subs":
            msg = {"op": "subscribe", "topic": "/hello"}
            websocket_c.send(json.dumps(msg))
        if send_command == "w":
            lo = {"linear": {"x": 0.2}, "angular": {"z": 0}}
            msg = {"op": "publish", "topic": "/cmd_vel_mux/input/navi", "type": "geometry_msgs/Twist", "msg": lo}
            websocket_c.send(json.dumps(msg))
        if send_command == "s":
            lo = {"linear": {"x": -0.2}, "angular": {"z": 0}}
            msg = {"op": "publish", "topic": "/cmd_vel_mux/input/navi", "type": "geometry_msgs/Twist", "msg": lo}
            websocket_c.send(json.dumps(msg))
        if send_command == "a":
            lo = {"linear": {"x": 0}, "angular": {"z": 1}}
            msg = {"op": "publish", "topic": "/cmd_vel_mux/input/navi", "type": "geometry_msgs/Twist", "msg": lo}
            websocket_c.send(json.dumps(msg))
        if send_command == "d":
            lo = {"linear": {"x": 0}, "angular": {"z": -1}}
            msg = {"op": "publish", "topic": "/cmd_vel_mux/input/navi", "type": "geometry_msgs/Twist", "msg": lo}
            websocket_c.send(json.dumps(msg))
        if send_command == "k":
            lo = {"linear": {"x": 0}, "angular": {"z": 0}}
            msg = {"op": "publish", "topic": "/cmd_vel_mux/input/navi", "type": "geometry_msgs/Twist", "msg": lo}
            websocket_c.send(json.dumps(msg))
        print ("Command done with no msg back")

if __name__ == '__main__':
    main()

    