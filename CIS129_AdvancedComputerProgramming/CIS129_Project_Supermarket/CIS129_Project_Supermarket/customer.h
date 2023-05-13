#pragma once
using namespace std;

class Customer
{
private:
	string Username;

	double Balance;

public:
	Customer(string username, double balance=0);

	//Property Retrieving
	double getBalance();

	//Property Altering Functions
	void topup(double topUpAmount);
	void pay(double payAmount);
};

