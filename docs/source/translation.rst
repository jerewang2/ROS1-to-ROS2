Translation
===========

.. _publishers:

Publishers
----------

 Description for Test 1

ROS1 Example

.. code-block:: console

   1 #include <dynamic_reconfigure/server.h>
   2 #include <geometry_msgs/PoseStamped.h>
   3 #include <kr_mav_controllers/SO3Config.h>
   4 #include <kr_mav_controllers/SO3Control.h>

ROS2 Example

.. code-block:: console

   # Invalid permalink

===========

.. _subscribers:

Subscribers
-----------

 Description for Test 2

ROS1 Example

.. code-block:: console

   38  private:
   39   void publishSO3Command();
   40   void position_cmd_callback(const kr_mav_msgs::PositionCommand::ConstPtr &cmd);
   41   void odom_callback(const nav_msgs::Odometry::ConstPtr &odom);
   42   void enable_motors_callback(const std_msgs::Bool::ConstPtr &msg);
   43   void corrections_callback(const kr_mav_msgs::Corrections::ConstPtr &msg);
   44   void cfg_callback(kr_mav_controllers::SO3Config &config, uint32_t level);

ROS2 Example

.. code-block:: console

   53   Eigen::Vector3f des_pos_, des_vel_, des_acc_, des_jrk_, config_kx_, config_kv_, config_ki_, config_kib_, kx_, kv_;
   54   float des_yaw_, des_yaw_dot_;
   55   float current_yaw_;
   56   bool enable_motors_, use_external_yaw_, have_odom_;
   57   float kR_[3], kOm_[3], corrections_[3];
   58   float mass_;
   59   const float g_;
   60   Eigen::Quaternionf current_orientation_;

===========
