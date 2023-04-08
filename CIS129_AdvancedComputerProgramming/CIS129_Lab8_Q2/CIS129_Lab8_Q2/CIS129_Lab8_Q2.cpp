// CIS129_Lab8_Q2.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include "checksum.h"
using namespace std;

void init(int arr[], int NUM_DIGIT);
void readInput(int arr[], int NUM_DIGIT);
bool digitValid(int arr[], int NUM_DIGIT);
void displayInput(int arr[], int NUM_DIGIT);
const int NUM_DIGIT = 16;

int main()
{
	int credit_arr[NUM_DIGIT];
	int checksum = 0;
	bool numValid = false;

	while (!numValid) {
		init(credit_arr, NUM_DIGIT);
		readInput(credit_arr, NUM_DIGIT);
		numValid = digitValid(credit_arr, NUM_DIGIT);
	}

	displayInput(credit_arr, NUM_DIGIT);
	
	checksum = checksumCalc(credit_arr, NUM_DIGIT);
	cout << "The checksum of the credit card digits is: " << checksum << endl;
	cout << "The credit card number is ";
	if (checksumValid(checksum)) {
		cout << "Valid.";
	}
	else {
		cout << "Invalid.";
	}
}

void init(int arr[], int NUM_DIGIT) {
	for (int i = 0; i <= NUM_DIGIT - 1; i++) {
		arr[i] = -1;
	}
}

void readInput(int arr[], int NUM_DIGIT) {
	cout << "Please input a " << NUM_DIGIT << "-digit credit card number : " << endl;
	for (int i = 0; i <= NUM_DIGIT - 1; i++) {
		cin >> arr[i];
	}
}

bool digitValid(int arr[], int NUM_DIGIT) {
	for (int i = 0; i <= NUM_DIGIT - 1; i++) {
		if (arr[i] > 9 or arr[i] < 0) {
			cout << "Please input a digit with 0 to 9." << endl;
			return false;
		}
	}
	return true;
}

void displayInput(int arr[], int NUM_DIGIT) {
	cout << "The input credit card number:";
	for (int i = 0; i <= NUM_DIGIT - 1; i++) {
		if (i % 4 == 0) {
			cout << " " << arr[i];
		}
		else {
			cout << arr[i];
		}
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
