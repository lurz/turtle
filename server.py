#!/usr/bin/env python

import asyncio
import websockets
import rospy
from geometry_msgs.msg import Twist

class GoForward():
    def __init__(self):
        rospy.init_node('GoForward', anonymous=False)
        rospy.loginfo("To stop TurtleBot CTRL + C")
        rospy.on_shutdown(self.shutdown)
        self.cmd_vel = rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size=10)
        r = rospy.Rate(10)
        move_cmd = Twist()
        move_cmd.linear.x = 0.2
    	move_cmd.angular.z = 0
        while not rospy.is_shutdown():
            self.cmd_vel.publish(move_cmd)
            r.sleep()
                        
    def shutdown(self):
        rospy.loginfo("Stop TurtleBot")
        self.cmd_vel.publish(Twist())
        rospy.sleep(1)

@asyncio.coroutine
def start(websocket, path):
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
    print("go forward")
    GoForward()
    return True

def dob():
    print("b")
    return True

start_server = websockets.serve(start, '192.168.86.51', 8080)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
