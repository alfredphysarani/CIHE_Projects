#include <iostream>
#include <string>
#include "Header.h"
using namespace std;
//Represent the boss enemy in the game
Boss::Boss(string name) : Enemy(name)
{
    Name = name;
    //Set the attributes to be a higher value.
    Health = 300;
    MaxAttackPower = 30;
    EXPWorth = 200;
    Stun = false;
}