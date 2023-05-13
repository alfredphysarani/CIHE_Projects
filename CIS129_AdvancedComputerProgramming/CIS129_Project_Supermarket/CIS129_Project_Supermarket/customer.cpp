#include <iostream>
#include "customer.h"

Customer::Customer(string username, double balance) {
	Username = username;
	Balance = balance;
}

double Customer::getBalance() {
	return Balance;
}

void Customer::topup(double topUpAmount) {
	Balance += topUpAmount;
}

void Customer::pay(double payAmount) {
	Balance -= payAmount;
}
