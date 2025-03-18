Translation
=====

.. _publishers:

Publishers
------------

ROS1 Example

.. code-block:: console

   1 #!/usr/bin/env python
   2 # license removed for brevity
   3 import rospy
   4 from std_msgs.msg import String
   5 
   6 def talker():
   7     pub = rospy.Publisher('chatter', String, queue_size=10)
   8     rospy.init_node('talker', anonymous=True)
   9     rate = rospy.Rate(10) # 10hz
  10     while not rospy.is_shutdown():
  11         hello_str = "hello world %s" % rospy.get_time()
  12         rospy.loginfo(hello_str)
  13         pub.publish(hello_str)
  14         rate.sleep()
  15 
  16 if __name__ == '__main__':
  17     try:
  18         talker()
  19     except rospy.ROSInterruptException:
  20         pass

=====

.. _subscribers:

Subscribers
------------

ROS1 Example

.. code-block:: console

   1 #!/usr/bin/env python
   2 import rospy
   3 from std_msgs.msg import String
   4 
   5 def callback(data):
   6     rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
   7     
   8 def listener():
   9 
  10     # In ROS, nodes are uniquely named. If two nodes with the same
  11     # name are launched, the previous one is kicked off. The
  12     # anonymous=True flag means that rospy will choose a unique
  13     # name for our 'listener' node so that multiple listeners can
  14     # run simultaneously.
  15     rospy.init_node('listener', anonymous=True)
  16 
  17     rospy.Subscriber("chatter", String, callback)
  18 
  19     # spin() simply keeps python from exiting until this node is stopped
  20     rospy.spin()
  21 
  22 if __name__ == '__main__':
  23     listener()

=====