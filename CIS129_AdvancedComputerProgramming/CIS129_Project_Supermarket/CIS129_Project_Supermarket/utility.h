#pragma once
#include <exception>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cctype>
#include "product.h"
#include "customer.h"
using namespace std;

// Output Helper
void titleBeautifier(string title, int halfWidth, char boarderFiller, char titleFiller) {
	/*
		Purpose:
			- To print title of UI
		Argument:
			- title (string): the UI title to be displayed
			- halfWidth (int): the half-length of the width of the UI
			- boarderFiller (char): the character to be used to fill the boarder
			- titleFiller (char): the character to be used to fill the title line
		Return:
			- N/A
	*/
	int titleLen = title.size();
	int titleLFill = halfWidth + titleLen / 2;
	int titleRFill = halfWidth - titleLen / 2 - 1;
	cout << string(halfWidth*2, boarderFiller) << endl;
	cout << boarderFiller << string((halfWidth - 1)*2, ' ') << boarderFiller << endl;
	cout << boarderFiller << setfill('-') << setw(titleLFill) << title << setw(titleRFill) << boarderFiller << endl;
	cout << boarderFiller << string((halfWidth - 1) * 2, ' ') << boarderFiller << endl;
	cout << string(halfWidth * 2, boarderFiller) << endl;

}

void productList(Product arr[], int pageN, int itemPerPage, int totalNProduct) {

	int startN = (pageN - 1) * itemPerPage;
	int endN = pageN * itemPerPage;
	int totalPage = totalNProduct / itemPerPage + 1;

	cout << setw(5) << setfill('-') << "ID";
	cout << setw(20) << setfill('-') << "Product Name";
	cout << setw(20) << setfill('-') << "Price ($)";
	cout << setw(20) << setfill('-') << "Stock" << endl;

	for (int i = startN; i < endN; i++) {
		if (arr[i].getName() != "") {
			cout << setw(5) << setfill(' ') << arr[i].getID();
			cout << setw(20) << setfill(' ') << arr[i].getName();
			cout << fixed << showpoint;
			cout << setw(20) << setfill(' ') << setprecision(2) << arr[i].getPrice();
			cout << setw(20) << setfill(' ') << arr[i].getQty() << endl;
		}
	}
	cout << string(65, '-') << endl;
	cout << "Page " << pageN << " out of total " << totalPage << " page(s) " << endl;
	cout << endl;
}

int pageControl(char direction, int currentPage, int maxPage) {
	if (direction == 'p') {
		if (currentPage <= 1) {
			currentPage = maxPage;
		}
		else {
			currentPage -= 1;
		}
	}
	else {
		if (currentPage == maxPage) {
			currentPage = 1;
		}
		else {
			currentPage += 1;
		}
	}
	return currentPage;
}

// Input Helper
void fileOpenChecker(ifstream& inf) {
	if (!inf)
	{
		throw "Failed to open file";
	}
}

bool numChecker(string s) {
	for (int i = 0; i < s.size(); i++) {
		if (!isdigit(s[i]) && s[i] != '.') {
			return false;
		}
	}
	return true;
}

int spaceCounter(string line) {
	int nSpace = 0;
	for (int i = 0; i < line.size(); i++) {
		if (isspace(line[i])) {
			nSpace += 1;
		}
	}
	return nSpace;
}

string upperString(string s) {
	string upStr = "";
	for (int i = 0; i < s.size(); i++) {
		if (isalpha(s[i])) {
			upStr += toupper(s[i]);
		}
		else {
			upStr += s[i];
		}
	}
	return upStr;
}

void lineGrouper(string line, string lineObj[]) {
	int j = 0;
	lineObj[j] = "";
	
	for (int i = 0; i < line.size(); i++) {
		if (!isspace(line[i])) {
			lineObj[j] += line[i];
		}
		else {
			j += 1;
			lineObj[j] = "";
		}
	}
}

void productDBLineAnalyzer(string line, int& id, string& name, double& price, int& qty) {
	int iFirstNum, nSpace;
	string strPrice, strQty, strID;

	nSpace = spaceCounter(line);
	string* lineGroups = new string[nSpace+1];

	lineGrouper(line, lineGroups);
	id = stoi(lineGroups[0]);
	name = lineGroups[1];

	for (int i = 2; i < nSpace+1; i++) {
		if (!numChecker(lineGroups[i])) {
			name += " ";
			name += lineGroups[i];
		}
		else {
			iFirstNum = i;
			break;
		}
	}
	
	price = stod(lineGroups[iFirstNum]);
	qty = stoi(lineGroups[iFirstNum+1]);
}

bool inputValidator(char c, char option[], int nOption) {
	/* inputValidator: 
		Purpose:
			- To validate whether the user input matches with the valid options provided
		Argument:
			- c (char): the user input of option
			- option[] (array of char): the valid option
		Return:
			- boolean - true for matched response; false for invalid response

	*/

	// for each option, validate to see if it is equal to the user input
	for (int i = 0; i < nOption; i++) {
		if (isalpha(c)) 
		{
			if (toupper(c) == toupper(option[i])) {
				return true;
			}
		}
		else 
		{
			if (c == option[i]) {
				return true;
			}
		}
	}
	return false;
}

bool stringPartialMatch(string target, string searchString) {
	bool match = false;
	if (target.size() > searchString.size()) {
		return false;
	}
	else {
		string upTarget = upperString(target);
		string upSearchStr = upperString(searchString);
		for (int i = 0; i <= searchString.size() - target.size(); i++) {
			for (int j = 0; j < target.size(); j++) {
				if (upTarget[j] != upSearchStr[i + j]) {
					break;
				}
				else {
					match = true;
				}
			}
			if (match) {
				return true;
			}
		}
	}
	return false;
}



void selectionSort(Product arr[], string sortKey, char direction, int arrSize) {
	Product dumProd;

	for (int i = 0; i < arrSize; i++) {
		int mIndex = i;
		for (int j = i+1; j < arrSize; j++) {
			if (sortKey == "id") {
				if (direction == 'a') {
					if (arr[j].getID() < arr[mIndex].getID()) {
						mIndex = j;
					}
				}
				else {
					if (arr[j].getID() > arr[mIndex].getID()) {
						mIndex = j;
					}
				}
			}
			else if (sortKey == "name") {
				if (direction == 'a') {
					if (arr[j].getName() < arr[mIndex].getName()) {
						mIndex = j;
					}
				}
				else {
					if (arr[j].getName() > arr[mIndex].getName()) {
						mIndex = j;
					}
				}
			}
			else if (sortKey == "price") {
				if (direction == 'a') {
					if (arr[j].getPrice() < arr[mIndex].getPrice()) {
						mIndex = j;
					}
				}
				else {
					if (arr[j].getPrice() > arr[mIndex].getPrice()) {
						mIndex = j;
					}
				}
			}
			else if (sortKey == "qty") {
				if (direction == 'a') {
					if (arr[j].getQty() < arr[mIndex].getQty()) {
						mIndex = j;
					}
				}
				else {
					if (arr[j].getQty() > arr[mIndex].getQty()) {
						mIndex = j;
					}
				}
			}
		}
		dumProd = arr[i];
		arr[i] = arr[mIndex];
		arr[mIndex] = dumProd;
	}
}

int productSearchByID(Product arr[],int targetID, int totalNProduct) {
	int min = 0, half = 0, max = totalNProduct;
	bool found = false;
	while (!found && min <= max) {
		half = (min + max) / 2;
		if (targetID == arr[half].getID()) {
			found = true;
		}
		else if (targetID < arr[half].getID()) {
			max = half - 1;
		} 
		else {
			min = half + 1;
		}
	}
	if (found) {
		return half;
	}
	else {
		return -1;
	}
}

void productFilterByName(Product arr[], string targetStr, int totalNProduct) {
	Product* filteredProduct = new Product[totalNProduct];
	int j = 0;
	for (int i = 0; i < totalNProduct; i++) {
		if (stringPartialMatch(targetStr, arr[i].getName())) {
			filteredProduct[j] = arr[i];
			j += 1;
		}
	}

	if (j == 0) {
		cout << "No matched product." << endl;
	}
	else {
		cout << "Number of Matched Results: " << j << endl;
		productList(filteredProduct, 1, totalNProduct, totalNProduct);
	}
	delete[] filteredProduct;
}

int countProdArr(Product arr[], int totalNProduct) {
	int count = 0;
	for (int i = 0; i < totalNProduct; i++) {
		if (arr[i].getID() != -1) {
			count += 1;
		}
	}
	return count;
}

// Cart Manipulation
bool addToCart(Product arr[], Product cart[], int totalNProduct) {
	int selectID = 0, qty = 0, idx = 0, cartId = 0, cartN = 0;
	cout << "[Customer Action] Please input the ID of the product you want to purchase: " << endl;
	cin >> selectID;
	idx = productSearchByID(arr, selectID, totalNProduct);
	if (idx == -1) {
		cout << "[System Info] There is no existing product with ID " << selectID << "." << endl;
		return false;
	}

	cartN = countProdArr(cart, totalNProduct);

	cout << "[System Info] The product you selected is <" << arr[idx].getName() << ">." << endl;
	cout << "[System Info] The unit price is <$ " << arr[idx].getPrice() << ">." <<endl;

	if (arr[idx].getQty() == 0) {
		cout << "[System Info] The selected product " << arr[idx].getName() << " is sold out." << endl;
		return false;
	}

	cartId = productSearchByID(cart, selectID, totalNProduct);

	if (cartId != -1) {
		cout << "[System Info] The product is already in the shopping cart." << endl;
		cart[cartId].describe("cart");
		cout << "[System Info] The remainig quantity available in stock: " << arr[idx].getQty() - cart[cartId].getQty() << ">." << endl;
		if (arr[idx].getQty() - cart[cartId].getQty() == 0) {
			cout << "[System Info] No more stock available for "  << cart[cartId].getName() << " to be added" << endl;
			return false;
		}
		
		while (cart[cartId].getQty() + qty > arr[idx].getQty() || qty <=0) {
			cout << "[Customer Action] Please input the quantity to add into the cart: " << endl;
			cin >> qty;

			if (cart[cartId].getQty() + qty > arr[idx].getQty()) {
				cout << "[System Info] The total quantity " << cart[cartId].getQty() + qty << " is greater than the remaining stock " << arr[idx].getQty() << endl;
				cout << "[Customer Action] Please input the quantity to add into the cart: " << endl;
			}
			else if (qty <= 0) {
				cout << "[System Info] The quantity input " << qty << " is less than or equal to zero." << endl;
				cout << "[Customer Action] Please input the quantity to purchase: " << endl;
			}
			
		}
		cart[cartId].addQty(qty);
	}
	else {
		cout << "[System Info] The remainig quantity available: " << arr[idx].getQty() << endl;
		while (qty > arr[idx].getQty() || qty <= 0) {
			cout << "Please input the quantity to purchase: " << endl;
			cin >> qty;
			if (qty > arr[idx].getQty()) {
				cout << "[System Info] The quantity input " << qty << " is greater than the remaining stock " << arr[idx].getQty() << endl;
				cout << "[Customer Action] Please input the quantity to purchase: " << endl;
			}
			else if (qty <= 0) {
				cout << "[System Info] The quantity input " << qty << " is less than or equal to zero." << endl;
				cout << "[Customer Action] Please input the quantity to purchase: " << endl;
			}
			
		}
		for (int i = 0; i < totalNProduct; i++) {
			if (cart[i].getID() == -1) {
				cart[i] = Product(selectID, arr[idx].getName(), arr[idx].getPrice(), qty);
				cartN = i + 1;
				break;
			}
		}
	}
	
	selectionSort(cart, "id", 'a', totalNProduct);

	cout << "[System Info] Current Product in the Shopping Cart: " << endl;
	productList(cart, 1, totalNProduct, cartN);
	return true;
}

bool editCart(Product arr[], Product cart[], int totalNProduct) {
	int selectID = 0, qty = 0, idx = 0, cartId = 0, cartN = 0;
	cout << "[Customer Action] Please input the ID of the product you want to edit: " << endl;
	cin >> selectID;
	idx = productSearchByID(cart, selectID, totalNProduct);
	if (idx == -1) {
		cout << "[System Info] " << selectID << " does not match with any product ID in the shopping cart." << endl;
		return false;
	}

	cout << "[System Info] The product in the shopping cart to be edited: " << endl;
	cart[cartId].describe("cart");
	cout << "[System Info] The remainig quantity available in stock: " << arr[idx].getQty() - cart[cartId].getQty() << ">." << endl;

	cout << endl;

	cout << "[Customer Action] Please input: " << endl;
	cout << "1. positive integer for adding quantity to the cart" << endl;
	cout << "2. positive integer for removing quantity to the cart" << endl;
	cout << "Quantity change: ";

	cin >> qty;
	cout << endl;

	if (qty > 0) {

	}
	else if (qty < 0) {

	}

	cout << "[System Info] The remainig quantity available in stock: " << arr[idx].getQty() - cart[cartId].getQty() << ">." << endl;
	if (arr[idx].getQty() - cart[cartId].getQty() == 0) {
		cout << "[System Info] No more stock available for " << cart[cartId].getName() << " to be added" << endl;
		return false;
	}
	cout << "[Customer Action] Please input the quantity to add into the cart: " << endl;
	cin >> qty;
	while (cart[cartId].getQty() + qty > arr[idx].getQty()) {
		cout << "[System Info] The total quantity " << cart[cartId].getQty() + qty << " is greater than the remaining stock " << arr[idx].getQty() << endl;
		cout << "[Customer Action] Please input the quantity to add into the cart: " << endl;
		cin >> qty;
	}
	cart[cartId].addQty(qty);
}

double totalCheckOutValue(Product arr[], int totalNProduct) {
	double val = 0;
	for (int i = 0; i < totalNProduct; i++) {
		if (arr[i].getID() != -1) {
			val += arr[i].getPrice();
		}
		else {
			break;
		}
	}
	cout << "The total value of products: $ " << val << endl;
	return val;
}

void flowPauser() {
	string dum = "";
	cout << "[Customer Action] Please input any character to continue: ";
	cin >> dum;
	cout << "[Customer Action] Continue" << endl;
}