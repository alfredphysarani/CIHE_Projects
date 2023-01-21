// MoneyChangeProg.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

using namespace std;

int main()
{
    // variable assignment
    int cents, hdollar, quat, dime, nick, penn;

    // ask for user input for cents
    cout << "Enter change in cents: ";
    cin >> cents;

    cout << "The change you entered is " << cents<<endl;
    hdollar = cents / 50;
    cout << "The number of half-dollars to be returned is " << hdollar << endl;
    quat = cents % 50 / 25;
    cout << "The number of quaters to be returned is " << quat << endl;
    dime = cents % 50 % 25 / 10;
    cout << "The number of dimes to be returned is " << dime << endl;
    nick = cents % 50 % 25 % 10 / 5;
    cout << "The number of nickels to be returned is " << nick << endl;
    penn = cents % 50 % 25 % 10 % 5;
    cout << "The number of pennies to be returned is " << penn << endl;

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
