#include <iostream>
using namespace std;

int main() {
	int x;
	int y;
	int z;
	cout << "Please enter three integers: ";
	cin >> x >> y >> z;

	// case 1: all three equal
	if (x >= y && y >= z) {
		cout << x << " + " << z << " = " << x + z << endl;
	}
	else if (x >= z && z >= y) {
		cout << x << " + " << y << " = " << x + y << endl;
	}
	else if (y >= x && x >= z) {
		cout << y << " + " << z << " = " << y + z << endl;
	}
	else if (y >= z && z >= x) {
		cout << y << " + " << x << " = " << y + x << endl;
	}
	else if (z >= x && x >= y) {
		cout << z << " + " << y << " = " << z + y << endl;
	}
	else if (z >= y && y >= x) {
		cout << z << " + " << x << " = " << z + x << endl;
	}
	return 0;
}