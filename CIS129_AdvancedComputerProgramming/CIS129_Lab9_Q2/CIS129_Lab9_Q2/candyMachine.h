// class dispenserType
// This class specifies the members to implement a dispenser.

class dispenserType
{
    private:
    int numberOfItems; //variable to store the number of items in the dispenser
    int cost;          //variable to store the cost of an item
    
    public:
    dispenserType(int setNoOfItems , int setCost); 
    //Constructor 
    //Sets the cost and number of items of a product to the values specified by the user.
    
    int getNoOfItems() const; 
    //Function to return the number of items of a product in the machine.

    int getCost() const; 
    //Function to show the cost of a product.

    void makeSale();  
    //Function to reduce the number of items of a product by 1.

};

// class cashRegister
// This class specifies the members to implement a cash register.
 
class cashRegister
{
    private:
    int cashOnHand;     //variable to store the cash in the register
    
    public:
    void acceptAmount(int amountIn);
    //Function to receive the amount deposited by the customer and update the amount in the register.

};