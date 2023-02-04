// ConsoleApplication_Lecture1.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <string>
using namespace std;

int main()
{
	int x, y, sum;
	cout << "Please input two numbers: ";
	cin >> x >> y;
	sum = x + y;
	cout << "The solution of " << x << " + " << y << " is " << sum << endl;

	int n = 2147483647;
	cout << n + 1 << endl;

	string str, str_getline;
	cin >> str;
	getline(cin, str_getline);
	cout << "The word from cin: " << str << endl;
	cout << "The word from getline: " << str_getline << endl;

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
