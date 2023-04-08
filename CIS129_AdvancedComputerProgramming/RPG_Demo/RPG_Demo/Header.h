#include <string>
using namespace std;

class Player    
{
private:
    string Name;
    int Health;
    bool Dead = false;
    bool Guarding = false;
    int AttackLvFactor; // adding level factor for attack
    int HealLvFactor; // adding level factor for healing
    int MaxAttackPower;
    int MaxHealAmount;
    int Level;  // adding level
    int MaxLevel;  // adding level
    int EXP;
    string setMove[4]; // setMove
    void Die();

public:
    Player(string name);    
    string getName();
    int getMaxAttackPower();
    int getMaxHealAmount();
    bool IsDead();
    bool IsGuarding();
    void setGuarding(bool guard);
    void GetsHit(int hit_value);
    void Heal(int amount_to_heal);
    void LevelUp();
    void GetsEXP(int exp_amount);
    string GetSetMove(int index);
    void LearnMove(string moveName, int replace_index);
};

class Enemy
{
protected:
    string Name;
    int Health;
    bool Dead = false;
    int MaxAttackPower;
    int EXPWorth;
    void Die();
    bool Stun;

public:
    Enemy(string name);     
    string getName();
    int getMaxAttackPower();
    bool IsDead();
    int getEXPWorth();
    void GetsHit(int hit_value);
    void setStun(bool status);
    bool IsStun();
};

class Boss : public Enemy
{
public:
    Boss(string name);    
};