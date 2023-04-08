// Implementation file candyMachineImp.cpp 
// This file contains the definitions of the functions to implement the operations of the classes cashRegister and dispenserType.
 
#include <iostream>
#include "candyMachine.h"

using namespace std;

dispenserType::dispenserType(int setNoOfItems, int setCost)
{
    //Constructor 
    //Sets the cost and number of items of a product to the values specified by the user.

    if (setNoOfItems >= 0)
        numberOfItems = setNoOfItems;
    else    
        numberOfItems = 50;

    if (setCost >= 0)
        cost = setCost;
    else
        cost = 50;
}

int dispenserType::getNoOfItems() const
{
	//Function to return the number of items of a product in the machine.
    return numberOfItems;
}

int dispenserType::getCost() const
{
	//Function to show the cost of a product.
    return cost;
}

void dispenserType::makeSale()
{
	//Function to reduce the number of items of a product by 1.
    numberOfItems--;
}

void cashRegister::acceptAmount(int amountIn)
{
	//Function to receive the amount deposited by the customer and update the amount in the register.
    cashOnHand = cashOnHand + amountIn;
}