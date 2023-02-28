// CIS129_Lab5_Q1.cpp : This file contains the 'main' function. Program execution begins and ends there.
//
#include <iostream>
#include <iomanip>
using namespace std;
void getFloat(float arr[]);
void ascendingSort(float arr[], int length_arr);
void weightSumCalc(float arr[], int length_arr, float& sum);

int main()
{
	//Initialize
	float floatArr[5] = { 0., 0., 0., 0., 0. };
	float resultSum = 0.;

	getFloat(floatArr);
	ascendingSort(floatArr, 5);
	cout << "Arrange the floating point numbers in ascending order: \n";
	for (int i = 0; i < 5; i++) {
		cout << floatArr[i] << " ";
	}
	cout << endl << "\n";

	weightSumCalc(floatArr, 5, resultSum);

	cout << fixed << showpoint;
	cout << "Weighted sum = " << setprecision(1) << resultSum;

	return 0;
}

void getFloat(float arr[]) {
	cout << "Please enter 5 floating point numbers. \n";
	for (int i = 0; i < 5; i++) {
		cin >> arr[i];
	}
	cout << " \n";
}

void ascendingSort(float arr[], int length_arr) {
	int min = 0;
	float temp = 0;
	for (int i = 0; i < length_arr; i++) {
		min = i;
		for (int j = i + 1; j < length_arr; j++) {
			if (arr[j] < arr[min]) {
				min = j;
			}
		}
		temp = arr[i];
		arr[i] = arr[min];
		arr[min] = temp;
	}
}

void weightSumCalc(float arr[], int length_arr, float& sum) {
	for (int i = 0; i < length_arr; i++) {
		sum += (length_arr - i) * arr[i];
	}
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
