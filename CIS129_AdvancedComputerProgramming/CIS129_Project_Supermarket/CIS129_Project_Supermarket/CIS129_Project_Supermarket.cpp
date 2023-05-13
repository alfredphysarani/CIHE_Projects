// CIS129_Project_Supermarket.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

// include libraries
#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include "utility.h"
#include "product.h"
#include "customer.h"
#include "uiOptionControl.h"

// namespace define
using namespace std;

//Constant Variable Declaration
const int MAX_NO_OF_PRODUCT = 50;
const string productDBFile = "productLog.txt";

//function declaration
void init(ifstream& data, Product arr[], int& n);

int main()
{
	// Initialize Variables
	char opt; // for user input characters
	bool sysExit = false, login = false;
	bool lastSortID = false;
	int totalNProduct = 0;
	optionControl* optionCon;
	userTypeOption userTypeOpt;
	customerOption cusOpt;
	cartOption cartOpt;


	// Step 2: Open Product Information File 
	ifstream productDB;
	productDB.open(productDBFile);
	try {
		fileOpenChecker(productDB);
	}
	catch (const char* msg) {
		cerr << msg << endl;
		return 1;
	}

	// Step 3: Initiate Array of Product Object
	Product* productArr = new Product[MAX_NO_OF_PRODUCT];

	// Step 4: Read Product Info and Store to Array
	init(productDB, productArr, totalNProduct);

	productDB.close();

	selectionSort(productArr, "id", 'a', totalNProduct);
	lastSortID = true;

	// Step 5: Main UI Function
	while (!sysExit) {
		// Step 5a: Customer - Staff Option
		titleBeautifier("Welcome to Amasoon E-Shop System!", 50, '=', '-');
		optionCon = &userTypeOpt;
		opt = optionCon->optionGet();

		if (tolower(opt) == 'c') {
			login = true;
			Product* shoppingCart = new Product[totalNProduct];
			Customer currentCus("valued customer", 0);
			titleBeautifier("Welcome Customer", 50, '=', '-');
			int pageNo = 1, noOfItemPerPage = 10;
			int maxPage = totalNProduct / noOfItemPerPage + 1;
			productList(productArr, pageNo, noOfItemPerPage, totalNProduct);

			while (login) {
				bool cartShown = false;
				optionCon = &cusOpt;
				opt = optionCon->optionGet();


				if (opt == 'p') {
					pageNo = pageControl('p', pageNo, maxPage);
					productList(productArr, pageNo, noOfItemPerPage, totalNProduct);
				}
				else if (opt == 'n') {
					pageNo = pageControl('n', pageNo, maxPage);
					productList(productArr, pageNo, noOfItemPerPage, totalNProduct);
				}
				else if (opt == '1') {
					if (!lastSortID) {
						selectionSort(productArr, "id", 'a', totalNProduct);
					}
					addToCart(productArr, shoppingCart, totalNProduct);
					flowPauser();
					productList(productArr, pageNo, noOfItemPerPage, totalNProduct);
				}
				else if (opt == '2') {
					if (countProdArr(shoppingCart, totalNProduct) != 0) {
						productList(shoppingCart, 1, totalNProduct, countProdArr(shoppingCart, totalNProduct));
						cartShown = true;
						optionCon = &cartOpt;
					}
					else {
						cout << "[System Info] The shopping cart is empty. Return to the Customer Homepage. " << endl;
					}
					while (cartShown) {	
						opt = optionCon->optionGet();
						if (opt == 1) {
							editCart(productArr, shoppingCart, totalNProduct);
						}
						else if (opt == 2) {

						}
					}
					flowPauser();
					productList(productArr, pageNo, noOfItemPerPage, totalNProduct);
				}
				else if (opt == '3') {

				}
				else if (opt == 'x') {
					login = false;
					sysExit = true;
				}
			}

		}
		else {
			sysExit = true;
		}
	}
	return 0;
}


// Function to initialize the system
void init(ifstream& data, Product arr[], int& n) {
	string detail, prodName;
	int qty = 0;
	double price = 0;
	int id = -1;
	n = 0;

	while (getline(data, detail)) 
	{	
		productDBLineAnalyzer(detail, id, prodName, price, qty);
		arr[n] = Product(id, prodName, price, qty);
		n += 1;
	}
	cout << "[INFO] Successfully loading product data." << endl;
}

