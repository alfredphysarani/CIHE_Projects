// CIS129_Lab4_Q2.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <fstream>
using namespace std;

const int NO_OF_CAP_LETTER = 26;

void init(int arr[], int noOfItem);
void characterCount(ifstream& ipt, ofstream& opt, int letterCount[26], int& lineCount);
void writeTotal(ofstream& opt, int letterCount[26], int& lineCount);

int main()
{
    // declare variables
    int lineCount = 0;
    int letterCount[NO_OF_CAP_LETTER];
    
    init(letterCount, NO_OF_CAP_LETTER);

    // I/O File
    ifstream inFile;
    ofstream outFile;

    inFile.open("textin.txt");

    if (!inFile) {
        cout << "Failed to open the input file. Terminating the Program";
        return 1;
    }

    outFile.open("textout.out");
    if (!outFile) {
        cout << "Failed to open the output file. Terminating the Program";
        return 1;
    }

    characterCount(inFile, outFile, letterCount, lineCount);
    writeTotal(outFile, letterCount, lineCount);

    inFile.close();
    outFile.close();
    return 0;
}

void init(int arr[], int noOfItem) {
    for (int i = 0; i < noOfItem; i++) {
        arr[i] = 0;
    }
}

void characterCount(ifstream& ipt, ofstream& opt, int letterCount[26], int& lineCount) {
    char ch;
    int i;
    ipt.get(ch);
    while (ipt) {
        // directly output the characters to output file as we looping the chars
        opt << ch;
        if (isalpha(static_cast<unsigned char>(ch))) { // to handle unsigned characters (which will in the range of -255 to 255 like accented a, e, o, u in German
            i = static_cast<int>(toupper(ch)) - static_cast<int>('A');
            letterCount[i] += 1;
        }
        else if (ch == '\n') {
            // count the number of new line char
            lineCount += 1;
        }
        ipt.get(ch);
    }
    opt << endl;
}

void writeTotal(ofstream& opt, int letterCount[26], int& lineCount) {
    opt << "The number of lines = " << lineCount << endl;
    for (int i = 0; i < 26; i++) {
        opt << static_cast<char>(i + static_cast<int>('A')) << " Count = " << letterCount[i] << endl;
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
