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

   30   {
   31     controller_.resetIntegrals();
   32   }

===========

.. _subscribers:

Subscribers
-----------

 Description for Test 2

ROS1 Example

.. code-block:: console

   18  public:
   19   SO3ControlNodelet()
   20       : position_cmd_updated_(false),
   21         position_cmd_init_(false),
   22         des_yaw_(0),
   23         des_yaw_dot_(0),
   24         current_yaw_(0),
   25         enable_motors_(false),
   26         use_external_yaw_(false),
   27         have_odom_(false),
   28         g_(9.81),
   29         current_orientation_(Eigen::Quaternionf::Identity())
   30   {
   31     controller_.resetIntegrals();
   32   }

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
