// CIS128_Lab9_Q1.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include "ClassImp.cpp"

using namespace std;

int main()
{
    testClass test(1, 2);
    test.print();

    testClass test2;
    test2.print();

    testClass test3(5, 6);
    test3.print();

    testClass test4(5, 7, 4.5);
    test4.print();

    testClass test5(4, 9, 12);
    test5.print();

    testClass test6(3.4, 'D');
    test6.print();

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
