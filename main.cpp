// main.cpp
#include "SensorSimulator.h"

int main() {
    SensorSimulator simulator("sim.txt", ',');
    simulator.start();

    return 0;
}
