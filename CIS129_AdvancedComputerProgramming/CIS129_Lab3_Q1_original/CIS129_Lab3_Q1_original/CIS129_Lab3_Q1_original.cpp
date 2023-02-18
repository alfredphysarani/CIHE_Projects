// CIS129_Lab3_Q1.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
using namespace std;
void UpperHeart(int total_line);
void LowerHeart(int total_line);

int main()
{
    // if we can find the number of lines based on the size of heart using a function
    for (int nline = 0; nline < 5; nline++) {
        UpperHeart(nline);
    };

    for (int nline = 0; nline < 11; nline++) {
        LowerHeart(nline);
    };
    return 0;
}

void UpperHeart(int nline) {
    for (int j = 0; j < 5 - (nline + 1); j++) {
        cout << ' ';
    }
    for (int s = 0; s < 2 * nline + 3; s++) {
        cout << '*';
    }
    for (int j = 0; j < 2 * 5 - (2 * nline + 1); j++) {
        cout << ' ';
    }
    for (int s = 0; s < 2 * nline + 3; s++) {
        cout << '*';
    }
    for (int j = 0; j < 5 - (nline + 1); j++) {
        cout << ' ';
    }
    cout << endl;
}

void LowerHeart(int nline) {
    for (int j = 0; j < nline + 1; j++) {
        cout << " ";
    }
    for (int s = 0; s < 21 - 2*nline; s++) {
        cout << "*";
    }
    cout << endl;
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
