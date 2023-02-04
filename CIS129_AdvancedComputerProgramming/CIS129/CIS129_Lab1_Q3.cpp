// CIS129_Lab1_Q3.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int main()
{
    //Question 3
    float fac, interest, time;

    cout << "Please input the growth factor: ";
    cin >> fac;
    cout << "Please input interest rate: ";
    cin >> interest;

    cout << fixed;
    time = log10(fac) / log10(1 + interest / 100);
    cout << "Time required (0 d.p): " << setprecision(0) << time << " years \n";

    cout << showpoint;
    cout << "Time required (2 d.p): " << setprecision(2) << time << " years \n";

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
