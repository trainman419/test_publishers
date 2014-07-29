#!/usr/bin/env python

import math
import rospy

from mypkg.msg import TestArray

def main():
    rospy.init_node("test_pub")

    rate = rospy.Rate(5)
    pub = rospy.Publisher("array", TestArray)

    values = [ 0 ] * 4

    while not rospy.is_shutdown():
        # populate header
        m = TestArray()
        m.header.stamp = rospy.Time.now()

        t = m.header.stamp.to_sec()
        values[0] = math.sin(t)
        values[1] = math.cos(t)
        values[2] = math.sin(t + math.pi)
        values[3] = math.cos(t + math.pi)
        m.values = values
        pub.publish(m)
        rate.sleep()


if __name__ == '__main__':
    main()
