cmake_minimum_required(VERSION 3.8)
project(my_robot_interfaces)

find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED) # Mesaj üreticiyi bul

# Mesaj dosyasını tanıt
rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/Telemetry.msg"
)

ament_package()