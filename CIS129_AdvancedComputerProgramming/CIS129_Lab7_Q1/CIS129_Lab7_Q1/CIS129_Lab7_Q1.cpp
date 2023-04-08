// lab7
// Please complete the missing parts

#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>

using namespace std;

//Step 1
const int NO_OF_IDOLS = 6;
const int NO_OF_REGIONS = 4;
struct idolsRecord {
    string idolsName;
    double votesByRegion[NO_OF_REGIONS];
    double totalVotes;
};

// Step 3
void initialize(idolsRecord idol[], int listSize);

// Step 6
void printHeading(ofstream& outdata);

// Step 6
void printResults(ofstream& outdata, idolsRecord idol[], string win, int largestVotes, int sumVotes, int listSize);

int main()
{
    //Step 1
    idolsRecord idols[NO_OF_IDOLS];

    string winner = "?????";
    int winner_vote = 0;
    int totalVote_AllRegion = 0;
    //Step 2
    ofstream outfile;
    string outputFile;

    //Step 3
    bool inputValidator = false;
    
    while (!inputValidator) {
        bool isExtension = false;
        cout << "Please input the name of the output file: ";
        cin >> outputFile;

        
        //Check if the input file string contains extension (can convert it into a function)
        for (int i = 0; i < outputFile.length(); i++) {
            if (outputFile[i] == '.') {
                isExtension = true;
                break;
            }
        }

        if (isExtension) {
            if (outputFile.length() <= 4) {
                cout << endl << "Please input a valid extension of fils as .out." << endl;
            }
            else {
                if (outputFile.substr(outputFile.length() - 4) == ".out") {
                    inputValidator = true;
                }
                else {
                    cout << endl << "Please input the extension of fils as .out." << endl;
                }
            }
        }
        // auto convert the extension if the input string does not contain any extension
        else {
            outputFile += ".out";
            inputValidator = true;
        }
    }
    
    //Step 4
    outfile.open(outputFile.c_str());
    if (!outfile) {
        cout << "Failed to open the file. Terminating the Program";
        outfile.close();
        return 1;
    }

    // Step 5
    initialize(idols, NO_OF_IDOLS);

    // Step 6
    printHeading(outfile);

    printResults(outfile, idols, winner, winner_vote, totalVote_AllRegion, NO_OF_IDOLS);

    // Step 7
    outfile.close();
    return 0;
}

//Step 5
void initialize(idolsRecord idol[], int idolSize)
{
    for (int i = 0; i < idolSize; i++) {
        idol[i].idolsName = "?????";
        for (int j = 0; j < NO_OF_REGIONS; j++) {
            idol[i].votesByRegion[j] = 0;
        }
        idol[i].totalVotes = 0;
    }
}

//Step 6
void printHeading(ofstream& outdata)
{
    outdata << setw(50) << setfill('-') << "\"My favourite idol\" Election Results" << setw(10) << setfill('-') << "-" << endl << endl;
    outdata << setw(38) << setfill(' ') << "Votes" << endl;
    outdata << "Idol Name" << setw(15) << "Region1" << setw(10) << "Region2" << setw(10) << "Region3"
        << setw(10) << "Region4" << setw(9) << "Total" << endl;
    outdata << setw(17) << setfill('-') << "   " << setw(10) << setfill('-') << "   "
        << setw(10) << setfill('-') << "   " << setw(10) << setfill('-') << "   "
        << setw(10) << setfill('-') << "   " << setw(9) << setfill('-') << "   " << endl;
}

//Step 6
void printResults(ofstream& outdata, idolsRecord idol[], string win, int largestVotes, int sumVotes, int listSize)
{
    int i, j;

    for (i = 0; i < listSize; i++)
    {
        outdata << left;
        outdata << setw(11) << setfill(' ') << idol[i].idolsName << "  ";
        outdata << right;
        for (j = 0; j < NO_OF_REGIONS; j++)
            outdata << setw(8) << idol[i].votesByRegion[j] << "  ";
        outdata << setw(8) << idol[i].totalVotes << endl;
    }

    outdata << endl << endl << "Winner: " << win
        << ", Votes Received: " << largestVotes
        << endl << endl;
    outdata << "Total votes polled: " << sumVotes << endl;
}
