#include <iostream>
#include "inputHelper.h"

inputChoice::inputChoice(int setNoOfChoices, string setChoicePurpose, char setArrChoice[], string setArrChoiceDesc[])
{
	noOfChoices = setNoOfChoices;
	choicePurpose = setChoicePurpose;
	for (int i = 0; i <= noOfChoices; i++)
	{
		arrChoice[i] = setArrChoice[i];
		arrChoiceDesc[i] = setArrChoiceDesc[i];
	}
}

void inputChoice::displayChoices()
{
	cout << choicePurpose << endl;
	for (int i = 0; i <= noOfChoices; i++) {
		cout << arrChoice[i] << ": " << arrChoiceDesc[i] << endl;
	}
	cout << "Please type in the correspoding character and press Enter to Proceed: ";
	// cin >> userChoice;
}