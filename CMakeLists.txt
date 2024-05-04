cmake_minimum_required(VERSION 2.8.3)
project(yolov8_ros)

find_package(catkin REQUIRED COMPONENTS
  rospy
  message_generation
  std_msgs
  sensor_msgs
  message_filters
)

## System dependencies are found with CMake's conventions
#find_package(catkin REQUIRED COMPONENTS std_msgs sensor_msgs message_generation)


## Uncomment this if the package has a setup.py. This macro ensures
## modules and global scripts declared therein get installed
## See http://ros.org/doc/api/catkin/html/user_guide/setup_dot_py.html
catkin_python_setup()

add_message_files(
  FILES
    Vector2.msg
    Point2D.msg
    Pose2D.msg
    Mask.msg
    KeyPoint3DArray.msg
    KeyPoint3D.msg
    KeyPoint2DArray.msg
    KeyPoint2D.msg
    DetectionArray.msg
    Detection.msg
    BoundingBox2D.msg
    BoundingBox3D.msg
)

generate_messages(
  DEPENDENCIES
  std_msgs
  sensor_msgs
)

catkin_package(CATKIN_DEPENDS
  message_runtime
  message_filters
#  INCLUDE_DIRS include
#  LIBRARIES yolov8_ros
#  CATKIN_DEPENDS rospy
#  DEPENDS system_lib
)

###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(
  ros/include
# include
  ${catkin_INCLUDE_DIRS}
)

#############
## Install ##
#############


#set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

#add_executable(detectron_sync src/detectron_sync.cpp)
#add_dependencies(detectron_sync ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
#target_link_libraries(detectron_sync ${catkin_LIBRARIES})

#install(TARGETS detectron_sync
#   RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
# )


foreach(dir ros)
    install(DIRECTORY ${dir}/
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir}
        USE_SOURCE_PERMISSIONS)
endforeach(dir)

## Mark executable scripts (Python etc.) for installation
## in contrast to setup.py, you can choose the destination
install(PROGRAMS
  src/yolov8_ros
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

## Mark cpp header files for installation
install(DIRECTORY
  msg
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
