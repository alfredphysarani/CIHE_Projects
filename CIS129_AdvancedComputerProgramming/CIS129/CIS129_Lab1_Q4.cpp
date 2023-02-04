// CIS129_Lab1_Q4.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    //Question 4
    int num_a, num_b;
    cout << "Please input first number: ";
    cin >> num_a;
    cout << "Please input second number: ";
    cin >> num_b;

    float half_a = num_a / 2.0;
    float half_b = num_b / 2.0;

    cout << fixed << showpoint;
    cout << "Average: " << setprecision(2) << num_a / 2.0 + num_b / 2.0;

    return 0;
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
