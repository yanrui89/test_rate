#! /usr/bin/env python
import rospy
from test_rate.msg import pva


class publisher():
    def __init__(self):
        self.pva_pub = rospy.Publisher("pva_topic", pva, queue_size=1)
        self.pva_timer = rospy.Timer(rospy.Duration(0.1), self._publishing)

    def _publishing(self, msg):
        print("hello")
        curr_pva = pva()
        curr_pva.position.x = 1
        curr_pva.position.y = 2
        
        self.pva_pub.publish(curr_pva)


    


if __name__ == "__main__":
    rospy.init_node("publishing_node")
    publisher()
    rospy.spin()
