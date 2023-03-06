#! /usr/bin/env python
import rospy
from test_rate.msg import pva





class listener():
    def __init__(self):
        rospy.Subscriber("pva_topic",pva, self._pva_callback)

    def _pva_callback(self,msg):
        print(msg.position.x)


if __name__ == "__main__":
    rospy.init_node("listener_node")
    listener()
    rospy.spin()

