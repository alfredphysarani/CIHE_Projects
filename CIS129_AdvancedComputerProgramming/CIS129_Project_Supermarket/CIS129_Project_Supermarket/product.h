#pragma once
using namespace std;

class Product
{
private:
	string Name;

	int ID;
	int Qty;
	double Price;
	double DiscountPct;

public:
	Product(int id = -1, string Name = "", double p = 0.0, int q = 0);

	//Property Retrieving
	int getID();
	string getName();
	double getPrice();
	int getQty();

	//Property Altering Functions
	void setPrice(double p);
	void setQty(double q);
	void addQty(double addQ);
	void deductQty(double deductQ);
	void describe(string mode);
};

