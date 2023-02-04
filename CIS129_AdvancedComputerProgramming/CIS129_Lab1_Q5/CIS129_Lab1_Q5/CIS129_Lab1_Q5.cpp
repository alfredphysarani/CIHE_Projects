// CIS129_Lab1_Q5.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <iomanip>
#include <string>
using namespace std;

int main()
{
    //Question 5
    string movie_name;
    float adult_p, child_p, perc_donate, gross, donated;
    int adult_sold, child_sold;

    cout << "Enter movie name: ";
    getline(cin, movie_name);
    cout << "Enter the price of an adult ticket: ";
    cin >> adult_p;
    cout << "Enter the price of a child ticket: ";
    cin >> child_p;
    cout << "Enter number of adult tickets sold: ";
    cin >> adult_sold;
    cout << "Enter number of child tickets sold: ";
    cin >> child_sold;
    cout << "Enter the percentage of donation: ";
    cin >> perc_donate;

    gross = adult_sold * adult_p + child_sold * child_p;
    donated = gross * perc_donate / 100.0;
    

    cout << "-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*" << endl;
    cout << setw(36) << setfill('.') << left << "Movie Name: " << setw(18) << setfill(' ') << right << movie_name << endl;
    cout << setw(36) << setfill('.') << left << "Number of Tickets Sold: " << setw(15) << setfill(' ') << right << adult_sold + child_sold << endl;
    cout << fixed << showpoint;
    // The setw(n) for the price with precision of 2 -> right will align the decimal point -> setw(n-2)
    cout << setw(36) << setfill('.') << left << "Gross Amount: " << " $" << setw(13) << setfill(' ') << right << setprecision(2) << gross << endl;
    cout << setw(36) << setfill('.') << left << "Percentage of Gross Amount Donated: " << setw(15) << setfill(' ') << right << setprecision(2) << perc_donate << " %" << endl;
    cout << setw(36) << setfill('.') << left << "Amount Donated: " << " $" << setw(13) << setfill(' ') << right << setprecision(2) << donated << endl;
    cout << setw(36) << setfill('.') << left << "Net Sale: " << " $" << setw(13) << setfill(' ') << right << setprecision(2) << gross - donated << endl;

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
