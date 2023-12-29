# CMakeLists.txt
cmake_minimum_required(VERSION 3.12)
project(SensorSimulator)

set(CMAKE_CXX_STANDARD 11)

include_directories(include)

add_executable(SensorSimulator main.cpp src/SensorSimulator.cpp)
