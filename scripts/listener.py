#! /usr/bin/env python
import rospy
from test_rate.msg import pva




class listener():
    def __init__(self):
        rospy.Subscriber("pva_topic",pva, self._pva_callback)
        self.count = 0
        self.time = 0
        self.freq_count = 0

    def _pva_callback(self,msg):
        # print(msg.position.x)
        # print(msg.header.stamp.secs)
        time = rospy.Time.now()
        if self.count == 0:
            self.time = time

        count = msg.position.x
        pub_time = msg.header.stamp
        # Find difference in time
        delta_time = pub_time.secs - time.secs

        if time.secs - self.time.secs != 0:
            print(f"The frequency received is {self.freq_count}")
            self.freq_count = 1
            self.time = time

        self.freq_count += 1

        if delta_time != 0:
            print(f"Time delay in {count} by {delta_time}")
        if self.count == 0:
            self.count = count
        if count != self.count:
            print(f"{count} not received")
            self.count = count - 1
        self.count += 1
        print(self.count)


if __name__ == "__main__":
    rospy.init_node("listener_node")
    listener()
    rospy.spin()

