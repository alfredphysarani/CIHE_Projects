#include <iostream>
#include <string>
#include "Header.h"
using namespace std;
Enemy::Enemy(string name)
{
    Name = name;
    Health = 100;
    MaxAttackPower = 10;
    EXPWorth = 100;
    Stun = false;
}

//return enemy's name
string Enemy::getName() {
    return Name;
}

//check if the enemy's is dead
bool Enemy::IsDead() {
    return Dead;
}

//return enemy maximum attack power
int Enemy::getMaxAttackPower() {
    return MaxAttackPower;
}

int Enemy::getEXPWorth() {
    return EXPWorth;
}

//This gets called when the enemy is hit.
// The amount of damage the enemy will take.
void Enemy::GetsHit(int hit_value)
{
    //Subtract the hit value from health.
    Health = Health - hit_value;

    if (Health < 0)
    {
        Health = 0;
    }

    //Write out that the enemy got hit
    cout << "[Enenmy HP Update] " << Name << " was hit for " << hit_value << " damage! He now has " << Health << " health remaining." << endl;
    //Check if the enemy is dead.
    if (Health <= 0)
    {
        //The enemy is dead.
        Die();
    }
}

//Called when the enemy is supposed to die
void Enemy::Die()
{
    //Write to the console that the enemy is dead
    cout << Name << " has died!" << endl;
    //Set the boolean that this enemy has died
    Dead = true;
}

void Enemy::setStun(bool status)
{
    Stun = status;
}

bool Enemy::IsStun() {
    return Stun;
}
