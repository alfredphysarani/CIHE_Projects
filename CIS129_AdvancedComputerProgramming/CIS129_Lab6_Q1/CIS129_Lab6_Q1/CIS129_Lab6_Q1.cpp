// CIS129_Lab6_Q1.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int main()
{
    int n = 0;
    double sum = 0, mean = 0, sd = 0, sum_d = 0;
    double* arr = new double[n];
    cout << "How many numbers would you like to input?" << endl;
    cin >> n;

    cout << "Enter " << n << " numbers" << endl;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
        sum += arr[i];
    }

    mean = sum / n;
    for (int i = 0; i < n; i++) {
        sum_d += pow(arr[i] - mean, 2);
    }

    sd = sqrt(sum_d/n);
    
    cout << fixed << showpoint;
    cout << "Mean = " << setprecision(2) << mean << endl;
    cout << "Standard Deviaion = " << setprecision(2) << sd << endl;
    delete[] arr;
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
