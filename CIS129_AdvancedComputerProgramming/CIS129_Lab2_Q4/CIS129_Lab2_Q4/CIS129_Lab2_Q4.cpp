#include <iostream>
#include <iomanip>
#include <string>
#include <fstream>

using namespace std;

int main() {
	ifstream inFile;
	ofstream outFile;

	string firstName, lastName;
	double total = 0;
	double n = 0;

	inFile.open("test.txt");
	if(!inFile) {
		cout << "Failed to open the file. Terminating the Program";
		return 1;
	}
	
	outFile.open("testavg.out");

	outFile << "Student name: ";
	inFile >> firstName >> lastName;
	outFile << firstName << " " << lastName << endl;
	outFile << "Test scores:";

	outFile << fixed << showpoint;
	
	// from the Question requirement there are 5 scores
	// using a for loop to input the score 5 times
	for (int i = 0; i < 5; i++) {
		string score;
		inFile >> score;
		// just in case if we encounter any non-digits and in case the number starts with .
		if (isdigit(score[0]) || score[0] == '.') {
			outFile << " " << setprecision(2) << stod(score);
			total += stod(score);
			n++; // to see how many scores we have counted 
		}
	}
		
	outFile << endl;
	outFile << "Average test score: " << setprecision(2) << total/n<< endl;

	inFile.close();
	outFile.close();

	return 0;
}