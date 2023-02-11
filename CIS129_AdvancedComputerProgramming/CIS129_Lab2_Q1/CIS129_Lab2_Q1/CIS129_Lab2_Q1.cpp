#include <iostream>
using namespace std;

int main() {
	int x, y, z, min, max;
	cout << "Please enter three integers: ";
	cin >> x >> y >> z;

	if (x >= y) {
		max = x;
		min = y;
	}
	else {
		max = y;
		min = x;
	}

	if (z >= max) {
		max = z;
	}
	else if (z <= min) {
		min = z;
	}
	cout << max << " + " << min << " = " << max + min << endl;

	return 0;
}