#include <iostream>
#include <fstream>
#include <vector>
using namespace std;


// TODO: Not really sure how to deal with the threading or the blocks of groups
// to run in parallel. What I have here is simply a start 
// (see schema explanation below)


/**
 * Contains the block of information associated
 * with each line in a sim file
 */
struct simLine {
    string type; // The type of sensor
    int pin; // The pin associated with the sim line
    int min; // The min value to generate
    int max; // The max value to generate
    int duration; // Length of the simulation (in s)
    int frequency; // Amount of time between generation of a new value (in ms)
}

/**
 * The sensor simulator reads from a sim file, generates random values between 
 * a min and max, and produces sensor readings specified by those lines in parallel
 * that simulate behavior seen inside the real system running
 * 
 * This simulator is intended to help test the Agresso software system
 * without the need of actual hardware.
 * 
 * Schema for each simulation file:
 * 
 * Each line contains one of the following:
 * 1. sensor_type,pin,min,max,duration,frequency
 * 2. end
 * 
 * If the line is of group 1, that line specifies the type of the sensor,
 * the pin of the sensor, the min value of the generated values, the max
 * value of the generated values, how long to simulate this line for 
 * (in seconds), and how often to generate a value (in miliseconds).
 * 
 * If the line is of group 2, that specifies the end of a block of lines to 
 * simulate in parallel. If there are more lines in group 1 below end, that group
 * will be run in parallel following the conclusion of the last block.
 */
class SensorSimulator {
public:
    SensorSimulator(const string file_path, char delimeter) {
        file_path_ = file_path;
        delimeter_ = delimeter;
    }

    /**
     * Reads from the file and starts generating random values
     * based on the lines contained in the sim file
     */
    void start() {
        // Specify the beginning of running the simulator
        _running = true;

        // Read from the text file
        ifstream sim_file(file_path_);

        // Read the file line by line and begin simulating that line
        string line;
        while (getLine(sim_file, line)) {
            struct simLine data = readSimLine(line);
            simulateSensor(data);
        }

        // Close the text file
        sim_file.close();
    }

private:
    string file_path_;
    bool running_;
    char delimeter_;

    /**
     * Simulates the sensor for the particular line
     * @param simLine The simLine struct that contains the information 
     * from the line that was parsed
     * TODO: Need to write the actual random generator portion
     * and add it as a thread to run in parallel
     */
    void simulateSensor(struct simLine) {
        
    }

    /**
     * Constructs a simulation line struct from a line inside the sim file
     * @param line A line from the simulation file
     * @returns A simulation line object
     */
    struct simLine readSimLine(string line) {
        // TODO: Not sure how to deal with this part yet
        if(line == "end") {

        }

        else {
            vector<string> values = split(line);
            struct simLine data = {
                values[0],
                atoi(values[1]),
                atoi(values[2]),
                atoi(values[3]),
                atoi(values[4])
            }
        }

       return data;
    }

    /**
     * Splits the strings using a delimeter
     * @param s The string to split
     * @returns List of strings split by the delimeter
     */
    vector<string> split(string s)
    {
        string tmp = "";
        vector<string> values;

        // Loop through the sim line, read until each delimeter,
        // and add it to the list of strings to return
        for(int i = 0; i < s.length(); i++) {
            if(s[i] != delimeter_) {
                tmp.append(s[i])
            }
            else {
               values.push_back(tmp);
               tmp = "";
            }
        }

        // Add the very last entry
        values.push_back(tmp);

        return values;
    }

};