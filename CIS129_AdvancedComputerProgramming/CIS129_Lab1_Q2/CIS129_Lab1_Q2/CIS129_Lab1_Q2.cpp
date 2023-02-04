// CIS129_Lab1_Q2.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
using namespace std;

int main()
{
    //Question 2
    float ft, inc, totalinc;
    cout << "Enter two integers, one for feet and one for inches: ";
    cin >> ft >> inc;

    cout << "The number you entered are " << ft << " feet and " << inc << " inches \n";
    totalinc = 12.0 * ft + inc;
    cout << "The total number of inches = " << totalinc << endl;
    cout << "The number of centimeters = " << totalinc * 2.54 << endl;
    
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
