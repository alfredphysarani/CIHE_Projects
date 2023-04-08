#include <iostream>
#include <string>
#include "Header.h"
using namespace std;
Player::Player(string name)
{
    Name = name;
    //Set the health value to 100.
    Health = 100;
    Level = 1;
    HealLvFactor = 3;
    AttackLvFactor = 2;
    HealLvFactor = 3;
    MaxAttackPower = 10;
    MaxHealAmount = 30;
    MaxLevel = 5;
    EXP = 0;
    setMove[0] = "Attack";
    setMove[1] = "Multi Attack";
    setMove[2] = "Guard";
    setMove[3] = "Heal";
}

//return player's name
string Player::getName() {
    return Name;
}

//check if the player's is dead
bool Player::IsDead() {
    return Dead;
}

//return player's guarding statues
bool Player::IsGuarding() {
    return Guarding;
}

//change player's guarding statues
void Player::setGuarding(bool guard) {
    Guarding = guard;

}

//return player maximum attack power
int Player::getMaxAttackPower() {
    //cout << "[Debug] MaxAttackPower: " << MaxAttackPower << endl;
    return MaxAttackPower;
}

//return player maximum heal amount
int Player::getMaxHealAmount() {
    //cout << "[Debug] MaxHealAmount: " << MaxHealAmount << endl;
    return MaxHealAmount;
}

//This gets called when the player is hit.
// The amount of damage the player will take.
void Player::GetsHit(int hit_value)
{
    //Subtract the hit value from health.
    Health = Health - hit_value;

    if (Health < 0)
    {
        Health = 0;
    }

    //Write out that the player got hit
    cout << "[Player HP Change] " << Name << " was hit for " << hit_value << " damage! You now have " << Health << " health remaining." << endl;

    //Check if the player is dead.
    if (Health <= 0)
    {
        //The player is dead.
        Die();
    }
}

// Heals the player with the amount to heal
//The number amount to heal the player.
void Player::Heal(int amount_to_heal)
{
    //Heal the player by adding the amount to heal to the player's health.
    Health = Health + amount_to_heal;
    if (Health > 100)
    {
        Health = 100;
    }

    // Let the player know his new health value
    cout << "[Player HP Change] " << Name << " has healed " << amount_to_heal << " health. You now have " << Health << " health remaining." << endl;
}

//Called when the player is supposed to die
void Player::Die()
{
    //Set the boolean that this player has died
    Dead = true;
}

//Called when Level up
void Player::LevelUp()
{
    Level += 1;
    MaxAttackPower += AttackLvFactor;
    MaxHealAmount += HealLvFactor;
}

//Called when player defeat enemy and get Experience
void Player::GetsEXP(int exp_amount)
{
    if (Level < MaxLevel) 
    {
        cout << "[Player EXP&Lv] You gain " << exp_amount << " exp!" << endl;
        EXP += exp_amount;
        cout << "[Player EXP&Lv] Your current total exp: " << exp_amount << endl;

        if (EXP / 100 >= Level)
        {
            for (int i = Level; i <= EXP / 100; i++) {
                LevelUp();
                cout << "[Player EXP&Lv] You have level up to level " << Level << endl;
                if (Level == 3) 
                {
                    LearnMove("Smite", 0);
                    cout << "[Player Move Update] Smite can deal double the damage of Attack at Max, with a 50 % chance to stun the enemy!" << endl;
                }
                else if (Level == 5)
                {
                    LearnMove("Ultimate", 1);
                    cout << "[Player Move Update] Ultimate is a hidden sword skill of 10 combos!" << endl;
                }
            }
        }
    }
    else {
        cout << "[Player EXP&Lv] You are at Max Level. No More EXP gain" << endl;
    }

}

//Get Player Set Move
string Player::GetSetMove(int index) {
    return setMove[index];
}

void Player::LearnMove(string moveName, int replace_index) {
    string oldMoveName = setMove[replace_index];
    setMove[replace_index] = moveName;
    cout << "[Player Move Update] " << oldMoveName << " is replaced by " << moveName << endl;
}