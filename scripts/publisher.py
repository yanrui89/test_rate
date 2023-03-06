#! /usr/bin/env python
import rospy
from test_rate.msg import pva


class publisher():
    def __init__(self):
        self.pva_pub = rospy.Publisher("pva_topic", pva, queue_size=1)
        self.pva_timer = rospy.Timer(rospy.Duration(0.1), self._publishing)
        self.count = 0

    def _publishing(self, msg):
        print("hello")
        time = rospy.Time.now()
        curr_pva = pva()
        print(time)
        curr_pva.header.stamp = time
        curr_pva.position.x = self.count
        self.count += 1
        self.pva_pub.publish(curr_pva)


    


if __name__ == "__main__":
    rospy.init_node("publishing_node")
    publisher()
    rospy.spin()
