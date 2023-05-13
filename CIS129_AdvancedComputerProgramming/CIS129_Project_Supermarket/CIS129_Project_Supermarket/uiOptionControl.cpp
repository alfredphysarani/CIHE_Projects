#include <iostream>
#include "uiOptionControl.h"
using namespace std;

bool optionControl::optionValidator(char c, char arr[], int nOption) {
	//cout << "[Debug] User Options: " << c << endl;
	for (int i = 0; i < nOption; i++) {
		//cout << "[Debug] Compare: " << arr[i] << endl;
		if (isalpha(c))
		{
			if (toupper(c) == toupper(arr[i])) {
				return true;
			}
		}
		else
		{
			if (c == arr[i]) {
				return true;
			}
		}
	}
	return false;
}

char userTypeOption::optionGet() {
	cout << "[User Action] Please input one of the following character to proceed:" << endl;
	for (int i = 0; i < nOption; i++) {
		cout << "'" << options[i] << "' for " << descriptions[i] << endl;
	}

	char userInput;
	bool valid = false;
	while (!valid) {
		cout << "Input: ";
		cin >> userInput;
		cout << endl;
		valid = optionValidator(userInput, options, nOption);
		if (!valid) {
			cout << "please input a valid option." << endl;
			for (int i = 0; i < nOption; i++) {
				cout << "'" << options[i] << "' for " << descriptions[i] << endl;
			}
		}
	}
	return userInput;
}

char customerOption::optionGet() {
	cout << "[Customer Action] Valued customer, Please input one of the following options for different functions:" << endl;
	for (int i = 0; i < nOption; i++) {
		cout << "'" << options[i] << "' for " << descriptions[i] << endl;
	}

	char userInput;
	bool valid = false;
	while (!valid) {
		cout << "[Customer Action] Input: ";
		cin >> userInput;
		cout << endl;
		valid = optionValidator(userInput, options, nOption);
		if (!valid) {
			cout << "[System Info] please input a valid option." << endl;
			for (int i = 0; i < nOption; i++) {
				cout << "'" << options[i] << "' for " << descriptions[i] << endl;
			}
		}
	}
	return userInput;
}

char cartOption::optionGet() {
	cout << "[Customer Action] Valued customer, Please input one of the following options for different functions:" << endl;
	for (int i = 0; i < nOption; i++) {
		cout << "'" << options[i] << "' for " << descriptions[i] << endl;
	}

	char userInput;
	bool valid = false;
	while (!valid) {
		cout << "Input: ";
		cin >> userInput;
		cout << endl;
		valid = optionValidator(userInput, options, nOption);
		if (!valid) {
			cout << "please input a valid option." << endl;
			for (int i = 0; i < nOption; i++) {
				cout << "'" << options[i] << "' for " << descriptions[i] << endl;
			}
		}
	}
	return userInput;
}