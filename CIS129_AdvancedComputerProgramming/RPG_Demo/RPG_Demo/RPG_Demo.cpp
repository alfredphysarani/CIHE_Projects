/*
1. Separate Start Game Function to First Encounter to display the name of enemy encounter
2. Added EXP Level System with new moves learnt at level 3 and level 5 and paremeters level up (currently is hard coded, 
can improve by adding a class file to store moves)
3. Used Dynamic Array to generate queue of Small Enemy
4. Introduced new move "Smite" with Stun Abilities -> added Stun, setStun and IsStun to the class of enemy
5. Added endGame Function
*/

#include <iostream>
#include <iomanip>
#include <string>
#include <cstdlib>
#include <ctime>
#include <string>
#include "Header.h"

using namespace std;
void StartGame(string playerName, Player player);
void FirstEncounter(Player player, Enemy currentEnemy);
void SelectAction(int& playeraction, Player player);
void PerformActionwithEnemy(int playeraction, Player& player, Enemy& currentEnemy);
void endGame();
const int N_NORM_ENEMY = 4;
const string NAME_ENEMY[N_NORM_ENEMY] = { "Giant Enemy Crab", "Giant Enemy Shrimp", "Giant Enemy Fish", "Giant Enemy PogChamp" };

int main() {
    string name;
    int action;
    
    cout << "Please enter your name: ";
    getline(cin, name);
    cout << endl;

    //Assign the player name.

    Player knight(name);
    StartGame(name, knight);

    // Use Temporarily Array to Gen Enemy Class
    for (int i = 0; i < N_NORM_ENEMY; i++) {
        Enemy* temp_enemy = new Enemy(NAME_ENEMY[i]);
        FirstEncounter(knight, temp_enemy[0]);
        while (!temp_enemy[0].IsDead() && !knight.IsDead()) {
            SelectAction(action, knight);
            PerformActionwithEnemy(action, knight, temp_enemy[0]);
        }
        delete temp_enemy;
    }
    
    Boss big_boss("Big Boss");
    FirstEncounter(knight, big_boss);
    while (!big_boss.IsDead() && !knight.IsDead()) {
        SelectAction(action, knight);
        PerformActionwithEnemy(action, knight, big_boss);
    }

    endGame();

    return 0;
}
// separate into two function
void StartGame(string playerName, Player player)
{
    //Write out the start game text to the textbox.
    cout << "Thank you for entering your name, " << player.getName() << "." << endl;
}

void FirstEncounter(Player player, Enemy currentEnemy)
{
    //Write the text that we encountered the giant enemy crab.
    cout << player.getName() << " you have encountered a " << currentEnemy.getName() << "!" << endl << "What would you like to do?" << endl;
}

void SelectAction(int& playeraction, Player player) {
    cout << "Player Turn";
    cout << endl;
    for (int i = 0; i < 4; i++) {
        cout << setw(15) << setfill('-') << left << player.GetSetMove(i) << i+1 << endl;
    }
    cin >> playeraction;
    cout << endl;
}
void PerformActionwithEnemy(int playeraction, Player& player, Enemy& currentEnemy)
{
    cout << typeid(currentEnemy).name() << endl;
    //Create an initial hit value variable.
    int hit_value = 0;
    int amount_to_heal = 0;
    int stun_active = 0;
    //Check what action the player took
    switch (playeraction)
    {
    case 1:
        //Write out the attack text.
        cout << "[Player Action] You choose to "<< player.GetSetMove(0) <<" the " << currentEnemy.getName() << "!" << endl;
        if (player.GetSetMove(0) == "Attack") {
            //Set the hit value.
            hit_value = (rand() + time(0)) % player.getMaxAttackPower() + 1;
            //Attack the enemy.
            currentEnemy.GetsHit(hit_value);
            break;
        }
        else if (player.GetSetMove(0) == "Smite") {
            //Set the hit value to double the attack
            hit_value = ((rand() + time(0)) % player.getMaxAttackPower() + 1) * 2;
            // Chance of Stunning Enemy
            stun_active = (rand() + time(0)) % 2; //either 0 or 1

            //Attack the enemy.
            currentEnemy.GetsHit(hit_value);
            
            // Stun Enemy
            if (stun_active) {
                currentEnemy.setStun(true);
            }
        }
        break;
        
    case 2:
        //Task 1: please write some codes to perform multi attack
        cout << "[Player Action] You choose to " << player.GetSetMove(1) << " the " << currentEnemy.getName() << "!" << endl;

        if (player.GetSetMove(1) == "Multi Attack") {
            for (int i = 0; i < 3; i++) {
                hit_value = (rand() + time(0)) % player.getMaxAttackPower() + 1;
                //Attack the enemy.
                currentEnemy.GetsHit(hit_value);
                if (currentEnemy.IsDead()) {
                    break;
                }
            }
        }
        else if (player.GetSetMove(1) == "Ultimate") {
            // 10 strikes ultimate
            for (int i = 0; i < 10; i++) {
                hit_value = (rand() + time(0)) % player.getMaxAttackPower() + 1;
                //Attack the enemy.
                currentEnemy.GetsHit(hit_value);
                if (currentEnemy.IsDead()) {
                    break;
                }
            }
        }
        break;
    case 3:
        //Task 2: please write some codes to guard
        cout << "[Player Action] You choose to defend!" << endl;

        player.setGuarding(true);

        break;
    case 4:
        //Task 3: please write some codes to heal
        cout << "[Player Action] You choose to Heal!" << endl;

        amount_to_heal = (rand() + time(0)) % player.getMaxHealAmount() + 1;
        //Attack the enemy.
        player.Heal(amount_to_heal);

        break;
    default:
        break;
    }

    //Task 4: please write some codes for enemyfs turn.Assume that the enemy only knows(single) attack.
    if (!currentEnemy.IsDead()) {
        cout << "Enemy Turn" << endl;
        if (player.IsGuarding()) {
            cout << "[Enemy Turn] " << player.getName() << " guarded the blow and was unharmed!" << endl;
            player.setGuarding(false);
        }
        else if (currentEnemy.IsStun()) {
            cout << "[Enemy Turn] " << currentEnemy.getName() << " is stunned and cannot move!" << endl;
            currentEnemy.setStun(false);
        }
        else {
            cout << "[Enemy Turn] " << currentEnemy.getName() << " choose to single attack you!" << endl;
            //Set the hit value.
            hit_value = (rand() + time(0)) % currentEnemy.getMaxAttackPower() + 1;
            //Attack the enemy.
            player.GetsHit(hit_value);
        }
    }

    //Task 5: Please write some codes to check if the player loose the game.
    if (player.IsDead()) {
        cout << "You have died. GAME OVER!!!" << endl;
    }

    //Task 6: Please write some codes to check if the player win the game.
    if (currentEnemy.IsDead()) {
        cout << "Congradulations " << player.getName() << ", you defeated the enemy" << endl;
        player.GetsEXP(currentEnemy.getEXPWorth());
    }
}

void endGame() {
    cout << "Congradulations! You have defeated all the enemeies and the big Boss!" << endl;
}