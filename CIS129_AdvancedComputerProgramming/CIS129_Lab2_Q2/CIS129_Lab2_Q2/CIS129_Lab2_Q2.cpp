#include <iostream>
using namespace std;

int main() {
	int a;
	int b;
	int c;
	int divis_count = 0;
	
	do {
		cout << "Please input the smallest integer in the range, a: ";
		cin >> a;
		cout << "Please input the largest integer in the range, b: ";
		cin >> b;

		if (b < a) {
			cout << "The largest integer b in the range must be greater than the smallest integer a \n";
		}
	} while (b < a);

	do {
		cout << "Please input the dividing integer, c: ";
		cin >> c;

		if (c <= 0) {
			cout << "Please input a positive integer for c. \n";
		}
	} while (c <= 0);

	cout << "Finding the divisible from " << a << " to " << b << endl;
	cout << "The integer to divide: " << c << endl;

	for (int x = a; x <= b; x++) {
		if (x % c == 0) {
			cout << x << " *\n";
			divis_count++;
		}
		else {
			cout << x << endl;
		}
	}

	if (divis_count == 0) {
		cout << "No divisible integer within range.";
	}
	return 0;
}