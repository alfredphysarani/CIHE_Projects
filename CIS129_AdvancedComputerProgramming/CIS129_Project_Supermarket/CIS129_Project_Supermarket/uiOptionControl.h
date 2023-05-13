#pragma once
#include <exception>
using namespace std;

class optionControl
{
protected:
	int nOption = 10;
	char options[10];
	string descriptions[10];
public:
	virtual char optionGet() = 0;
	bool optionValidator(char c, char arr[], int nOption);
};

class userTypeOption : public optionControl {
private:
	int nOption = 3;
	char options[3] = {'c', 's', 'x'};
	string descriptions[3] = {"customer login", "staff login", "exit"};
public:
	virtual char optionGet() override;
};

class customerOption : public optionControl {
private:
	int nOption = 6;
	char options[6] = { 'p', 'n', '1', '2', '3', 'x' };
	string descriptions[6] = { 
		"go to previuos page of product",
		"go to next page of product", 
		"add products to shopping cart",
		"show shopping carts and check-out",
		"search products",
		"exit"
	};
public:
	virtual char optionGet() override;
};

class cartOption : public optionControl {
private:
	int nOption = 5;
	char options[5] = { '1', '2', '3', '4', '5' };
	string descriptions[5] = {
		"edit product",
		"remove product",
		"clear cart"
		"check-out",
		"return to customer home page"
	};
public:
	virtual char optionGet() override;
};

class staffOption : public optionControl {
public:
	virtual char optionGet() override;
};

// Exit Flow
