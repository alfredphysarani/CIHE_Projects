#include <iostream>
using namespace std;

int main() {
	// if conditionals
	int x = 6;
	int y = 2;
	if (x > y) {
		cout << "x is greater than y \n";
	}
	else if (y > x) {
		cout << "y is greater than x \n";
	}
	else {
		cout << "x and y are equal \n";
	}

	// switch-case
	switch (x) {
	case 1:
		cout << "x equals to 1 \n";
		break;
	case 2:
	case 3:
		cout << "x equals to 2 or 3 \n";
		break;
	default:
		cout << "x is not equal to 1, 2 or 3 \n";
		break;
	}

	// Nested if 
	y = 0;
	if (x > y) {
		cout << "x is greater than y \n";
		if (x == 6) {
			cout << "x is equal to 6 \n";
		}
		else {
			cout << "x is not equal to 6 \n";
		}
	}
	else {
		cout << "x is not greater than y";
	}
	return 0;
}