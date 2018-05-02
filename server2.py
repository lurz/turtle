from websocket_server import WebsocketServer
import rospy
from geometry_msgs.msg import Twist

def GoForward():
    rospy.init_node('GoForward', anonymous=False)
    rospy.loginfo("To stop TurtleBot CTRL + C")
    cmd_vel = rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size=10)
    r = rospy.Rate(10)
    move_cmd = Twist()
    move_cmd.linear.x = 0.2
    move_cmd.angular.z = 0
    while not rospy.is_shutdown():
        self.cmd_vel.publish(move_cmd)
        r.sleep()
                        
def new_client(client, server):
    server.set_fn_message_received(message_received)

def message_received(client, server, message):
    print(message)
    if message == "forward":
        try:
            GoForward()
        except:
            rospy.loginfo("GoForward node terminated.")

server = WebsocketServer(8080, host='192.168.86.51')
server.set_fn_new_client(new_client)
server.run_forever()
