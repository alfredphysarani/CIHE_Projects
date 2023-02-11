#include <iostream>
#include <iomanip>
using namespace std;

int main() {
	double a;
	double r;
	double t;
	double sum = 0;
	int n = 1;

	do {
		cout << "Please enter the first term: ";
		cin >> a;

		if (a <= 0) {
			cout << "The first term input should be positive. \n";
		}
	} while (a <= 0);
	
	do {
		cout << "Please enter the common ratio: ";
		cin >> r;

		if (r <= 0 || r >= 1) {
			cout << "Please input a ratio > 0 and < 1 \n";
		}
	} while (r <= 0 || r >= 1);

	cout << fixed << showpoint;
	
	t = a;

	while (t > 0.01) {
		cout << n << " term = " << setprecision(4) << t << endl;
		sum += t;
		t = t * r;
		n++;
		if (t < 0.01) {
			cout << n << " term = " << setprecision(4) << t << endl;
			sum += t;
		}
	}

	cout << "Estimated Sum = " << sum << endl;
	cout << "Calculated Sum = " << a / (1 - r) << endl;

	return 0;
}