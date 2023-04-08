#include <iostream>
#include "candyMachine.h"

using namespace std;
void showseletion();
void sellProduct(dispenserType& product, cashRegister& pCounter);

int main()
{
	//Step 1
	cashRegister counter;

	//Step 2
	dispenserType candy(100, 50);
	dispenserType chips(2, 65);
	dispenserType gum(1, 60);
	dispenserType cookie(5, 20);

	//Step 3
	showseletion();

	//Step 4
	int selection = 0;

	//Step 5
	cin >> selection;

	//Step 6
	//  Change ### to the dispenserType defined in step 2
	//  Change ??? to a suitable variable or value
	while (selection != 9)
	{
		switch (selection)
		{
			//Step 6a
		case 1:
			sellProduct(candy, counter);
			break;
		case 2:
			sellProduct(chips, counter);
			break;
		case 3:
			sellProduct(gum, counter);
			break;
		case 4:
			sellProduct(cookie, counter);
			break;
		default:
			cout << "Invalid selection." << endl;
		}// end switch

		//Step 6b
		showseletion();

		//Step 6c
		cin >> selection;

	}//end while

	return 0;
}

//Step 3 and Step 6b
void showseletion()
{
	//Change ??? to the dispenserType defined in step 2
	cout << "*** Welcome to Candy shop ***" << endl;
	cout << "To select an item, enter" << endl;
	cout << "1 for Candy" << endl;
	cout << "2 for chips" << endl;
	cout << "3 for gum" << endl;
	cout << "4 for cookies" << endl;
	cout << "9 to exit" << endl;

}// end showelection

//Step 6a
void sellProduct(dispenserType& product, cashRegister& pCounter)
{
	int amount; //variable for storing amount deposited by the user
	//Step 6ai
	if (product.getNoOfItems() > 0)
	{
		cout << "Please deposit " << product.getCost() << " cents" << endl;
		cin >> amount;

	//Step 6aiI
		if (amount >= product.getCost())
		{
			product.makeSale();
			pCounter.acceptAmount(amount);
			cout << "Collect your item at the bottom and enjoy." << endl;
		}
	//Step 6aiII
		else {
			cout << "Please deposit another " << product.getCost() - amount << " cents" << endl;
			cout << "The amount is not enough. Collect what you deposited" << endl;
		}

	}// end if
	//Step 6aii
	else {
		cout << "Sorry, this item is sold out." << endl;
	}

	cout << "-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-" << endl << endl;
}// end sell product