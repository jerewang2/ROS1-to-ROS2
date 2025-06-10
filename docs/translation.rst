Translation
===========

.. _publishers:

Publishers
----------

Description for Test 1

.. code-block:: cpp

   #include <dynamic_reconfigure/server.h>
   #include <geometry_msgs/PoseStamped.h>
   #include <kr_mav_controllers/SO3Config.h>
   #include <kr_mav_controllers/SO3Control.h>

.. _test-2:

Test 2
------

Description for Test 2

.. code-block:: cpp

    private:
     void publishSO3Command();
     void position_cmd_callback(const kr_mav_msgs::PositionCommand::ConstPtr &cmd);
     void odom_callback(const nav_msgs::Odometry::ConstPtr &odom);
     void enable_motors_callback(const std_msgs::Bool::ConstPtr &msg);
     void corrections_callback(const kr_mav_msgs::Corrections::ConstPtr &msg);
     void cfg_callback(kr_mav_controllers::SO3Config &config, uint32_t level);

