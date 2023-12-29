// SensorSimulator.h
#ifndef SENSOR_SIMULATOR_H
#define SENSOR_SIMULATOR_H

#include <string>

struct simLine {
    // ... (unchanged)
};

class SensorSimulator {
public:
    SensorSimulator(const std::string& file_path, char delimeter);

    void start();

private:
    std::string file_path_;
    bool running_;
    char delimeter_;

    // ... (unchanged)
};

#endif // SENSOR_SIMULATOR_H
