// CIS129_Lab3_Q2.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <iomanip>
using namespace std;
double residential();
double business();

int main()
{
    int acc_num;
    double fee = 0;
    string cus_type;
    bool isValid = false;
    cout << fixed << showpoint;
    cout << "This program computes a cable bill. \n";
    
    while (!isValid) {
        cout << "Enter account number (an integer): ";
        cin >> acc_num;
        
        if (acc_num < 0) {
            cout << "Please enter a positive integer for account number. \n";
            continue;
        }
        isValid = true;
    }

    isValid = false;

    while (!isValid) {
        cout << "Enter customer type: R or r (Residential), B or b (Business): ";
        cin >> cus_type;

        if (cus_type == "b" || cus_type == "B") {
            fee = business();
            isValid = true;
        }
        else if (cus_type == "r" || cus_type == "R") {
            fee = residential();
            isValid = true;
        }
        else {
            cout << "Please enter customer type as R or r for residents, B or b as Business. \n";
            continue;
        }
    }

    cout << "Account number: " << acc_num << endl;
    cout << "Amount due: $" << setprecision(2) << fee << endl;
    return 0;
    
}

double residential() {
    int n_ch;
    bool isValid = false;
    while (!isValid) {
        cout << "Enter the number of premium channels: ";
        cin >> n_ch;

        if (n_ch < 0) {
            cout << "Please enter a positive integer for number of premium channels. \n";
            continue;
        }
        isValid = true;
    }

    return 20.5 + 4.5 + 7.5 * n_ch;
}

double business() {
    int n_ch, basic_conn;
    double basic_fee, premium_fee;
    bool isValid = false;

    while (!isValid) {
        cout << "Enter the number of basic service connections: ";
        cin >> basic_conn;
        
        if (basic_conn < 0) {
            cout << "Please enter a positive integer for number of basic service connections. \n";
            continue;
        }
        isValid = true;
    }

    if (basic_conn <= 10) {
        basic_fee = 75.0;
    }
    else {
        basic_fee = 75.0 + (basic_conn - 10.0) * 5.0;
    }

    isValid = false;

    while (!isValid) {
        cout << "Enter the number of premium channels: ";
        cin >> n_ch;

        if (n_ch < 0) {
            cout << "Please enter a positive integer for number of premium channels. \n";
            continue;
        }
        isValid = true;
    }

    premium_fee = 50.0 * n_ch;

    return premium_fee + basic_fee + 15.0;
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
