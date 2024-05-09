cmake_minimum_required(VERSION 3.5)
project(cpp_package)

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(example_interfaces REQUIRED)

add_executable(cpp_node src/first_node.cpp)
ament_target_dependencies(cpp_node rclcpp)

add_executable(cpp_publisher src/first_cpp_publisher.cpp)
ament_target_dependencies(cpp_publisher rclcpp example_interfaces)

add_executable(cpp_subscriber src/first_cpp_subscriber.cpp)
ament_target_dependencies(cpp_subscriber rclcpp example_interfaces)

add_executable(hw1_node src/hw1.cpp)
ament_target_dependencies(hw1_node rclcpp example_interfaces)

add_executable(hw2_node src/hw2.cpp)
ament_target_dependencies(hw2_node rclcpp example_interfaces)

install(TARGETS
  cpp_node
  cpp_publisher
  cpp_subscriber
  hw1_node
  hw2_node
  DESTINATION lib/${PROJECT_NAME})

ament_package()
