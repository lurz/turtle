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
        time.sleep(2)


def sendmsg(websocket_c, op_type, topic, msg_type, msg):
    send_msg = {}
    send_msg["op"] = op_type
    if op_type == "publish":
        send_msg["topic"] = topic
        send_msg["msg"] = msg
    if op_type == "subscribe":
        send_msg["topic"] = topic
    if op_type == "advertise":
        send_msg["topic"] = topic
        send_msg["type"] = msg_type
    websocket_c.send(json.dumps(send_msg))

def main():
    if len(sys.argv) != 2:
        print ("NEED IP ADDR")
        return
    server_ip = "ws://" + str(sys.argv[1]) + ":9090"
    websocket_c = create_connection(server_ip)

    rec_thread = threading.Thread(target=receivemsg, args=(websocket_c,))
    rec_thread.start()

    while True:
        send_command = input("Send command: ")
        if send_command == "exit":
            websocket_c.close()
            break
        if send_command == "hello":
            sendmsg(websocket_c, "publish", "/hello", "", {"data": "hello"})
        if send_command == "adver":
            sendmsg(websocket_c, "advertise", "/hello", "std_msgs/String", "")
        if send_command == "subs":
            sendmsg(websocket_c, "subscribe", "/hello", "", "")
        if send_command == "w":
            lo = {"linear": {"x": 0.2}, "angular": {"z": 0}}
            sendmsg(websocket_c, "publish", "/cmd_vel_mux/input/navi", "geometry_msgs/Twist", lo)
        if send_command == "s":
            lo = {"linear": {"x": -0.2}, "angular": {"z": 0}}
            sendmsg(websocket_c, "publish", "/cmd_vel_mux/input/navi", "geometry_msgs/Twist", lo)
        if send_command == "a":
            lo = {"linear": {"x": 0}, "angular": {"z": 1}}
            sendmsg(websocket_c, "publish", "/cmd_vel_mux/input/navi", "geometry_msgs/Twist", lo)
        if send_command == "d":
            lo = {"linear": {"x": 0}, "angular": {"z": -1}}
            sendmsg(websocket_c, "publish", "/cmd_vel_mux/input/navi", "geometry_msgs/Twist", lo)
        if send_command == "k":
            lo = {"linear": {"x": 0}, "angular": {"z": 0}}
            sendmsg(websocket_c, "publish", "/cmd_vel_mux/input/navi", "geometry_msgs/Twist", lo)
        print ("Command done with no msg back")

if __name__ == '__main__':
    main()
