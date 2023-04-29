using namespace std;

class inputChoice
{
private:
	int noOfChoices;
	string choicePurpose;
	char arrChoice[6] = {};
	string arrChoiceDesc[6] = {};
	char userChoice;

public:
	inputChoice(int setNoOfChoices, string setChoicePurpose, char setArrChoice[], string setArrChoiceDesc[]);
	void displayChoices();
};