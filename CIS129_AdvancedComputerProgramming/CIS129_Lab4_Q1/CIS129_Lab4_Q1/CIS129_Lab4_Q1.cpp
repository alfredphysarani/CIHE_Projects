// CIS129_Lab4_Q1.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
using namespace std;

// declare functions
void getNumber(int array[10]);
void classifyNumber(int array[10], int& n_zeros, int& n_odd, int& n_even);
void printResults(int& n_zeros, int& n_odd, int& n_even);


int main()
{    
    // declare variable
    int n_array[10];
    int n_zeros = 0;
    int n_odd = 0;
    int n_even = 0;

    // main function call
    getNumber(n_array);
    classifyNumber(n_array, n_zeros, n_odd, n_even);
    printResults(n_zeros, n_odd, n_even);
    return 0;
}

void getNumber(int array[10]) {
    cout << "Please enter 10 integers: " << endl;
    for (int i = 0; i < 10; i++) {
        cin >> array[i];
    }

    cout << "The numbers you entered are: " << endl;
    for (int i = 0; i < 10; i++) {
        cout << array[i] << " ";
    }
    cout << endl;
}

void classifyNumber(int array[10], int& n_zeros, int& n_odd, int& n_even) {
    for (int i = 0; i < 10; i++) {
        if (array[i] % 2 == 1 || array[i] % 2 == -1) {
            n_odd += 1;
        } 
        else {
            n_even += 1;
            if (array[i] == 0) {
                n_zeros += 1;
            }
        }
    }
}

void printResults(int& n_zeros, int& n_odd, int& n_even) {
    cout << "\n";
    cout << "The number of odd numbers is " << n_odd << endl;
    cout << "The number of even numbers is " << n_even << endl;
    cout << "The number of zeros is " << n_zeros << endl;
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
