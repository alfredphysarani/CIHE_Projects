// MoneyChangeProg.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

using namespace std;

const int hdollar_value = 50;
const int quat_value = 25;
const int dime_value = 10;
const int nick_value = 5;

int main()
{
    // variable assignment
    int change;

    // ask for user input for cents
    cout << "Enter change in cents: ";
    cin >> change;

    cout << "The change you entered is " << change <<endl;
    cout << "The number of half-dollars to be returned is " << change / hdollar_value << endl;
    change = change % hdollar_value;
    cout << "The number of quaters to be returned is " << change / quat_value << endl;
    change = change % quat_value;
    cout << "The number of dimes to be returned is " << change / dime_value << endl;
    change = change % dime_value;
    cout << "The number of nickels to be returned is " << change / nick_value << endl;
    change = change % nick_value;
    cout << "The number of pennies to be returned is " << change << endl;

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
