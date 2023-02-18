// CIS129_Lab3_Q3.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <iomanip>
#include <fstream>
#include <cmath>
using namespace std;
double calculateCourseAverage(ifstream& inp);
double calculateAverage(double total, double n);
void printResult(ofstream& out, string course_name, double grp_1_average, double grp_2_average);

int main()
{
    string course_name_group1, course_name_group2;
    ifstream inFile1;
    ifstream inFile2;
    ofstream outFile;
    double average_c_score_g1 = 0;
    double average_c_score_g2 = 0;
    double total_score_g1 = 0;
    double total_score_g2 = 0;
    int n_course = 0;

    inFile1.open("group1.txt");
    if (!inFile1) {
        cout << "Failed to open the file. Terminating the Program";
        return 1;
    }

    inFile2.open("group2.txt");
    if (!inFile2) {
        cout << "Failed to open the file. Terminating the Program";
        inFile1.close();
        return 1;
    }

    outFile.open("Lab3_Q3_partb.out");
    outFile << fixed << showpoint;
    outFile << setw(8) << setfill(' ') << left << "Course" << setw(50) << setfill(' ') << "Course Average" << endl;
    outFile << setw(8) << setfill(' ') << "ID"; 
    for (int i = 0; i <= 10; i++) {
        outFile << setw(5) << setfill(' ') << left << i*10;
    }
    
    outFile << endl;
    outFile << setw(8) << setfill(' ') << " ";

    for (int i = 0; i < 10; i++) {
        outFile << "|....";
    }

    outFile << "|" << endl;

    while (!inFile1.eof() && !inFile2.eof()) {
        inFile1 >> course_name_group1;
        inFile2 >> course_name_group2;
        cout << "Current Course for group 1: " << course_name_group1 << endl;
        cout << "Current Course for group 2: " << course_name_group2 << endl;
        if (course_name_group1 == course_name_group2) { // this method requires the text file of 2 group have the same order of course name, using array to store the name allow us to check later (but not using it now)
            n_course += 1;
            average_c_score_g1 = calculateCourseAverage(inFile1);
            average_c_score_g2 = calculateCourseAverage(inFile2);
            total_score_g1 += average_c_score_g1;
            total_score_g2 += average_c_score_g2;
            cout << "Average Score for " << course_name_group1 << " of group 1: " << average_c_score_g1 << endl;
            cout << "Average Score for " << course_name_group2 << " of group 2: " << average_c_score_g2 << endl;
            printResult(outFile, course_name_group1, average_c_score_g1, average_c_score_g2);
        }
        else {
            cout << "The course name is different for the two group, the score cannot be compared.";
            inFile1.close();
            inFile2.close();
            outFile.close();
            return 1;
        }
    }

    outFile << left << "Group 1 -- ****" << endl;
    outFile << left << "Group 2 -- ####" << endl;
    outFile << left << "Avg for group 1: " << setprecision(2) << calculateAverage(total_score_g1, n_course) << endl;
    outFile << left << "Avg for group 2: " << setprecision(2) << calculateAverage(total_score_g2, n_course) << endl;


    // closing files
    inFile1.close();
    inFile2.close();
    outFile.close();

    return 0;
}

double calculateAverage(double total, double n) {
    return total / n;
}

double calculateCourseAverage(ifstream& inp) {
    double n = 0;
    double score = 0;
    double total_score = 0;
    inp >> score;
    while (score != -999) {
        n += 1;
        total_score += score;
        inp >> score;
    }
    return calculateAverage(total_score, n);
}

void printResult(ofstream& out, string course_name, double grp_1_average, double grp_2_average) {
    int num_star = 0;
    int num_hash = 0;

    // by rounding after divided by 2 -> 83.22 should map to 84, while 82.6 should map to 82
    num_star = round(grp_1_average / 2) + 1;
    num_hash = round(grp_2_average / 2) + 1;
    

    out << setw(8) << setfill(' ') << course_name;
    for (int i = 0; i < num_star; i++) {
        out << "*";
    }
    out << endl;

    out << setw(8) << setfill(' ') << " ";
    for (int i = 0; i < num_hash; i++) {
        out << "#";
    }
    out << endl;
    out << " " << endl;
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
