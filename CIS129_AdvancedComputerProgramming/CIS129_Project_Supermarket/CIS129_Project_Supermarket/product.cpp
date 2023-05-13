#include <iostream>
#include "product.h"

using namespace std;

Product::Product(int id, string name, double p, int q) {
	ID = id;
	Name = name;
	Price = p;
	Qty = q;
}

int Product::getID(){
	return ID;
}

string Product::getName() {
	return Name;
}

double Product::getPrice() {
	return Price;
}

int Product::getQty() {
	return Qty;
}

void Product::setPrice(double p) {
	Price = p;
}

void Product::setQty(double q) {
	Qty = q;
}

void Product::addQty(double addQ) {
	Qty += addQ;
}

void Product::deductQty(double deductQ) {
	Qty -= deductQ;
}

void Product::describe(string mode) {
	if (mode == "cart") {
		cout << "Product Name: " << Name << " | Price: $ " << Price << " | Quantity in Cart: " << Qty << endl;
	}
	else {
		cout << "Product Name: " << Name << " | Price: $ " << Price << " | Quantity in Stock: " << Qty << endl;
	}
}