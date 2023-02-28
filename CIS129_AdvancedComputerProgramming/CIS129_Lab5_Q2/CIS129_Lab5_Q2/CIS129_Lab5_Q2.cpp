// CIS129_Lab5_Q2.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

// Global Variable Declaration
const int NO_OF_IDOLS = 6;
const int NO_OF_REGIONS = 4;

// Function Declaration
void getIdolsName(ifstream& inp, string iNames[], int noOfRows);
void sortIdolsName(string iNames[], int noOfRows);
void initialize(int vbRegion[][NO_OF_REGIONS], int tVotes[], int noOfRows);
void processVotes(ifstream& inp, string iNames[], int vbRegion[][NO_OF_REGIONS], int noOfRows);
int Search(string iNames[], int noOfRows, string name);
void addRegionsVote(int vbRegion[][NO_OF_REGIONS], int tVotes[], int noOfRows);
void Winner(string iNames[], int tVotes[], string& win, int& largestVotes, int noOfRows);
void totalVoteelection(int tVotes[], int& sumVotes, int noOfRows);
void printHeading();
void printResults(string iNames[], int vbRegion[][NO_OF_REGIONS], int tVotes[], string win, int largestVotes, int sumVotes, int noOfRows);

int main()
{
    string idolsName[NO_OF_IDOLS];
    int votesByRegion[NO_OF_IDOLS][NO_OF_REGIONS];
    int totalVotes[NO_OF_IDOLS];
    string winner = "?????";
    int winner_vote = 0;
    int totalVote_AllRegion = 0;
    ifstream inFile;
    
    inFile.open("IdolData.txt");
    if (!inFile) {
        cout << "Failed to open the file. Terminating the Programme.";
        return 1;
    }

    getIdolsName(inFile, idolsName, 6);

    sortIdolsName(idolsName, 6);

    inFile.close();
    inFile.clear();

    inFile.open("VoteData.txt");
    if (!inFile) {
        cout << "Failed to open the file. Terminating the Programme.";
        return 1;
    }

    initialize(votesByRegion, totalVotes, NO_OF_IDOLS);
    processVotes(inFile, idolsName, votesByRegion, NO_OF_IDOLS);
    addRegionsVote(votesByRegion, totalVotes, NO_OF_IDOLS);
    Winner(idolsName, totalVotes, winner, winner_vote, NO_OF_IDOLS);
    totalVoteelection(totalVotes, totalVote_AllRegion, NO_OF_IDOLS);
    printHeading();
    printResults(idolsName, votesByRegion, totalVotes, winner, winner_vote, totalVote_AllRegion, NO_OF_IDOLS);
    
    return 0;
}

// Step 3
void getIdolsName(ifstream& inp, string iNames[], int noOfRows) {
    string idolName = "";
    int i = 0;
    for (int i = 0; i < noOfRows; i++) {
        inp >> idolName;
        iNames[i] = idolName;
    }
}

// Step 4	
void sortIdolsName(string iNames[], int noOfRows) {
    string temp = "";
    int length_j = 0, length_min = 0;
    for (int i = 0; i < noOfRows; i++) {
        int min = i;
        for (int j = i + 1; j < noOfRows; j++) {
            if (iNames[j] < iNames[min]) {
                min = j;
            }
        }
        temp = iNames[i];
        iNames[i] = iNames[min];
        iNames[min] = temp;
    }
}

// Step 7
void initialize(int vbRegion[][NO_OF_REGIONS], int tVotes[], int noOfRows) {
    for (int i = 0; i < noOfRows; i++)
        for (int j = 0; j < NO_OF_REGIONS; j++) {
            vbRegion[i][j] = 0;
        }
            

    for (int i = 0; i < noOfRows; i++) {
        tVotes[i] = 0;
    }
}

// Step 8	
void processVotes(ifstream& inp, string iNames[], int vbRegion[][NO_OF_REGIONS], int noOfRows) {
    string idoName;
    int region;
    int noOfVotes;
    int loc;

    inp >> idoName;
    while (inp) {
        loc = Search(iNames, noOfRows, idoName);
        inp >> region >> noOfVotes;
        vbRegion[loc][region - 1] += noOfVotes;
        inp >> idoName;
    }
}


//Step 8.2.1
int Search(string iNames[], int noOfRows, string name) {
    int lb = 0, ub = noOfRows - 1, half = 0;
    bool found = false;

    while (!found && lb <= ub) {
        half = (lb + ub) / 2;
        if (name == iNames[half]) {
            found = true;
        }
        else if (name >= iNames[half]) {
            lb = half + 1;
        }
        else {
            ub = half - 1;
        }
    }
    return half;
}

// Step 9
void addRegionsVote(int vbRegion[][NO_OF_REGIONS], int tVotes[], int noOfRows) {
    for (int i = 0; i < noOfRows; i++) {
        for (int j = 0; j < NO_OF_REGIONS; j++) {
            tVotes[i] += vbRegion[i][j];
        }
    }
}

// Step 10
void Winner(string iNames[], int tVotes[], string& win, int& largestVotes, int noOfRows) {
    for (int i = 0; i < noOfRows; i++) {
        if (tVotes[i] > largestVotes) {
            win = iNames[i];
            largestVotes = tVotes[i];
        }
    }
}


// Step 11
void totalVoteelection(int tVotes[], int& sumVotes, int noOfRows) {
    for (int i = 0; i < noOfRows; i++) {
        sumVotes += tVotes[i];
    }
}

// Step 12
void printHeading() {
    cout << setw(50) << setfill('-') << "\"My favourite idol\" Election Results" << setw(10) << setfill('-') << "-" << endl << endl;
    cout << setw(38) << setfill(' ') << "Votes" << endl;
    cout << "Idol Name" << setw(15) << "Region1" << setw(10) << "Region2" << setw(10) << "Region3" << setw(10) << "Region4" << setw(9) << "Total" << endl;
    cout << setw(17) << setfill('-') << "   " << setw(10) << setfill('-') << "   "
        << setw(10) << setfill('-') << "   " << setw(10) << setfill('-') << "   "
        << setw(10) << setfill('-') << "   " << setw(9) << setfill('-') << "   " << endl;
}

// Step 13
void printResults(string iNames[], int vbRegion[][NO_OF_REGIONS], int tVotes[], string win, int largestVotes, int sumVotes, int noOfRows) {
    for (int i = 0; i < noOfRows; i++) {
        cout << left;
        cout << setw(11) << setfill(' ') << iNames[i] << "  ";
        cout << right;
        for (int j = 0; j < NO_OF_REGIONS; j++)
            cout << setw(8) << vbRegion[i][j] << "  ";
        cout << setw(8) << tVotes[i] << endl;
    }

    cout << endl << endl << "Winner: " << win
        << ", Votes Received: " << largestVotes
        << endl << endl;
    cout << "Total votes polled: " << sumVotes << endl;
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
