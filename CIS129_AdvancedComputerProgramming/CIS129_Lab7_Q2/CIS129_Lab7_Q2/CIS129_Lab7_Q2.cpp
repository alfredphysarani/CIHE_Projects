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

// Step 4
void getIdolsName(ifstream& inp, idolsRecord idol[], int listSize);

// Step 8	
void processVotes(ifstream& indata, idolsRecord idol[], int listSize);


// Step 9
void addRegionsVote(idolsRecord idol[], int listSize);

// Step 10
void Winner(idolsRecord idol[], string& win, int& largestVotes, int listSize);

// Step 11
void totalVoteelection(idolsRecord idol[], int& sumVotes, int listSize);

// Step 12
void printHeading(ofstream& outdata);

// Step 13
void printResults(ofstream& outdata, idolsRecord idol[], string win, int largestVotes, int sumVotes, int listSize);

int main()
{
    //Step 1
    ifstream infile;//input file variable
    ofstream outfile;//output file variable

    string inputFile;//holding the input file
    string outputFile;//holding the output file

    idolsRecord idols[NO_OF_IDOLS];

    string winner = "?????";
    int winner_vote = 0;
    int totalVote_AllRegion = 0;

    //Step 2
    cout << "Enter the file name contains idols name: ";
    cin >> inputFile;
    cout << endl;
    infile.open(inputFile.c_str());
    if (!infile) {
        cout << "Canot open the input file. " << endl;
        return 1;
    }
    // Step 3
    initialize(idols, NO_OF_IDOLS);

    // Step 4
    getIdolsName(infile, idols, NO_OF_IDOLS);

    // Step 5
    infile.close();
    infile.clear();

    // Step 6
    cout << "Enter the vote data file name: ";
    cin >> inputFile;
    cout << endl;
    infile.open(inputFile.c_str());
    if (!infile) {
        cout << "Canot open the input file. " << endl;
        return 1;
    }

    //Step 7
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

    outfile.open(outputFile.c_str());
    if (!outfile) {
        cout << "Canot open the output file. " << endl;
        return 1;
    }

    // Step 8
    processVotes(infile, idols, NO_OF_IDOLS);

    // Step 9
    addRegionsVote(idols, NO_OF_IDOLS);

    // Step 10
    Winner(idols, winner, winner_vote, NO_OF_IDOLS);

    // Step 11
    totalVoteelection(idols, totalVote_AllRegion, NO_OF_IDOLS);

    // Step 12
    printHeading(outfile);

    // Step 13
    printResults(outfile, idols, winner, winner_vote, totalVote_AllRegion, NO_OF_IDOLS);

    // Step 14
    infile.close();
    outfile.close();
    return 0;
}

//Step 3
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

//Step 4
void getIdolsName(ifstream& indata, idolsRecord idol[], int listSize)
{
    for (int i = 0; i < listSize; i++) {
        indata >> idol[i].idolsName;
    }    
}

//Step 8
void processVotes(ifstream& indata, idolsRecord idol[], int listSize)
{
    string idoName;
    int region;
    int noOfVotes;
    int loc;
    //Step 8.1
    indata >> idoName >> region >> noOfVotes;

    //Step 8.2		
    while (indata)
    {
        //Step 8.2.1
        for (int i = 0; i < listSize; i++) {
            if (idol[i].idolsName == idoName)
            {
                //Step 8.2.2 & 8.2.3
                idol[i].votesByRegion[region - 1] += noOfVotes;
                break;
            }
        }
        //Step 8.2.4
        indata >> idoName >> region >> noOfVotes;
    }
}


//Step 9
void addRegionsVote(idolsRecord idol[], int listSize)
{
    for (int i = 0; i < listSize; i++) {
        for (int j = 0; j < NO_OF_REGIONS; j++) {
            idol[i].totalVotes += idol[i].votesByRegion[j];
        }
    }
}

//Step 10
void Winner(idolsRecord idol[], string& win, int& largestVotes, int listSize)
{
    for (int i = 0; i < listSize; i++) {
        if (idol[i].totalVotes > largestVotes) {
            largestVotes = idol[i].totalVotes;
            win = idol[i].idolsName;
        }
    }
}

//Step 11
void totalVoteelection(idolsRecord idol[], int& sumVotes, int listSize)
{
    for (int i = 0; i < listSize; i++) {
       sumVotes += idol[i].totalVotes;
    }
}

//Step 12
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

//Step 13
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
