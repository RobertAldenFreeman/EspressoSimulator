// SensorSimulator.cpp
#include "SensorSimulator.h"
#include <iostream>
#include <fstream>
#include <vector>

SensorSimulator::SensorSimulator(const std::string& file_path, char delimeter) {
    file_path_ = file_path;
    delimeter_ = delimeter;
    running_ = false;
}

void SensorSimulator::start() {
    _running = true;
    // ... (unchanged)
}

// ... (unchanged)
