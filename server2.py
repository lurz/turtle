from websocket_server import WebsocketServer
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

def new_client(client, server):
    server.set_fn_message_received(message_received)

def message_received(client, server, message):
    print(message)
    if message == "forward":
        try:
            GoForward()
            server.send_message_to_all("succeed!")
        except:
            server.send_message_to_all("failed!")
    else:
        server.send_message_to_all("wrong command!")

server = WebsocketServer(8080, host='192.168.86.51')
server.set_fn_new_client(new_client)
server.run_forever()