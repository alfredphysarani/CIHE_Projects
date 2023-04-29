// CIS129_Project_Supermarket.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

// include libraries
#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include "inputHelper.h"

using namespace std;

//function declaration
void uiLogin();

int main()
{
	uiLogin();
	return 0;
}

// Function to initialize the system
void init() {
	// Show Login UI

}

void uiLogin() {
	cout << setw(50) << setfill('=') << endl;
	cout << '=' << setw(48) << setfill(' ') << '=' << endl;
	cout << '=' << setw(20) << setfill(' ') << "Welcome to Amasoon E-Shop System!" << setw(20) << setfill(' ') << '=' << endl;
	cout << '=' << setw(48) << setfill(' ') << '=' << endl;
	cout << setw(50) << setfill('=') << endl << endl;

	inputChoice userChoice(2, "Select the type of users", { 'c', 's' }, {"customer", "staff"});
	userChoice.displayChoices();
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
