// CIS129_Lab6_Q2.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
using namespace std;

// Define Global enum object
enum objectType { ROCK, PAPER, SCISSORS };

// Function Declaration
void displayRules();
bool validSelection(char selection);
objectType retrievePlay(char selection);
void convertEnum(objectType object);
objectType winningObject(objectType playl, objectType play2);
void gameResult(objectType play1, objectType play2, int& gameC, int& winC1, int& winC2);
void displayResults(int& gameC, int& winC1, int& winC2);

int main() {
	// Define parameters
	int gameCount = 0;
	int winCount1 = 0;
	int winCount2 = 0;
	char response;
	char selection1;
	char selection2;
	objectType play1;
	objectType play2;

	//Step 1
	displayRules();

	//Step 2
	cin >> response;

	//Step 3
	while (response == 'y' || response == 'Y') {
		bool valid_selection, valid_selection2;
		//Step 3
		cout << endl;

		do {
			//Step 3a
			cout << "Player 1 enter your choice: ";
			cin >> selection1;
			cout << endl;
			//Step 3b
			valid_selection = validSelection(selection1);
		} while (valid_selection != true);

		cout << endl;
		do {
			//Step 3c
			cout << "Player 2 enter your choice: ";
			cin >> selection2;
			cout << endl;
			//Step 3d
			valid_selection2 = validSelection(selection2);
		} while (valid_selection2 != true);

		//Step 4
		play1 = retrievePlay(selection1);

		play2 = retrievePlay(selection2);

		//Step 5
		gameResult(play1, play2, gameCount, winCount1, winCount2);


		//Step 6
		cout << endl;
		cout << "Enter Y/y to play the game: ";
		cin >> response;
		if (response != 'y' && response != 'Y') {
			break;
		}

	}//end of while true

	//Step 7
	displayResults(gameCount, winCount1, winCount2);
	return 0;
}
//end of main
//Step 1
void displayRules() {
	cout << "Welcome to the game of Rock, Paper and Scissors." << endl;
	cout << "This is a game for two players. For each game, each" << endl;
	cout << "player selects one of the objects, Rock, Paper or Scissors. " << endl;
	cout << "The rules for winning the game are:" << endl;
	cout << "1. If both players selects the same object, it is a tie. " << endl;
	cout << "2. Rock breaks Scissors: So player who selects Rock wins. " << endl;
	cout << "3. Paper covers Rock: So player who selects Paper wins." << endl;
	cout << "4. Scissors cuts Paper: So player who selects Scissors wins." << endl;
	cout << endl;

	cout << "Enter R or r to select Rock, P or p to select Paper, and S or s to select Scissors." << endl;
	cout << "Enter Y/y to play the game:";


}

//Step 3b and Step 3d
bool validSelection(char selection) {
	if (tolower(selection) == 'r' || tolower(selection) == 'p' || tolower(selection) == 's') {
		return true;
	}
	//Write some awesome code here
	return false;
}
//Step 4
objectType retrievePlay(char selection) {
	objectType object;
	//Write some awesome code here
	if (towlower(selection) == 'r') {
		object = ROCK;
	}
	else if (tolower(selection) == 'p') {
		object = PAPER;
	}
	else if (tolower(selection) == 's') {
		object = SCISSORS;
	}
	return object;
}

//Step 5
void gameResult(objectType play1, objectType play2, int& gameC, int& winC1, int& winC2) {
	objectType winnerObject;
	int winner = -1;
	//Step 5a
	if (play1 != play2) {
		//Step 5ai
		winnerObject = winningObject(play1, play2);

		//Step 5aii & Step 5aiii
		if (winnerObject == play1) {
			winC1 += 1;
			winner = 1;
		} else if (winnerObject == play2) {
			winC2 += 1;
			winner = 2;
		}

		//Step 5aiv
		cout << "Player 1 selected ";
		convertEnum(play1);
		cout << " and player 2 selected ";
		convertEnum(play2);
		cout << ". ";
		
		//Step 5av
		cout << "Player " << winner << " wins this game." << endl;
	}
	//Step 5b
	else {
		//Step 5bi
		cout << "Both players selected ";
		convertEnum(play1);
		cout << ".";

		//Step 5bii
		cout << " This game is a tie." << endl;

	}
	//Step 5c
	gameC += 1;
}

//Step 5ai
objectType winningObject(objectType play1, objectType play2) {
	if (play1 == ROCK) {
		if (play2 == PAPER) {
			return PAPER;
		}
		else if (play2 == SCISSORS) { // using else if to prevent some one using the function incorrectly 
			return ROCK;
		}
	}
	else if (play1 == PAPER) {
		if (play2 == SCISSORS) {
			return SCISSORS;
		}
		else if (play2 == ROCK) { // using else if to prevent some one using the function incorrectly (e.g. PAPER PAPER)
			return PAPER;
		}
	}
	else if (play1 == SCISSORS) {
		if (play2 == PAPER) {
			return SCISSORS;
		}
		else if (play2 == ROCK) {
			return ROCK;
		}
	}
}

//Step 5aiv & Step 5bi
void convertEnum(objectType object) {
	if (object == PAPER) {
		cout << "PAPER";
	}
	else if (object == SCISSORS) {
		cout << "SCISSORS";
	}
	else {
		cout << "ROCK";
	}
}

//Step 7
void displayResults(int& gameC, int& winC1, int& winC2) {
	cout << "The total number of plays: " << gameC << endl;
	cout << "The number of plays won by player 1: " << winC1 << endl;
	cout << "The number of plays won by player 2: " << winC2 << endl;
}