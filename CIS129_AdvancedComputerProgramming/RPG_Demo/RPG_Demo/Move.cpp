#include <iostream>
#include <string>
#include "Header.h"
using namespace std;

Move::Move(string name)
{
    Name = name;
}

string Move::getMoveName()
{
    return Name;

}

AttackMove::AttackMove(string name, int attackTime, int playerAttackFac, int critChance, float critFac) : Move(name)
{
    Name = name;
    //Set the attributes to be a higher value.
    AttackTime = attackTime;
    PlayerAttackFac = playerAttackFac;
    CritChance = critChance; // 0 - 100
    CritFac = critFac;
}

void AttackMove::Attack(Player player, Enemy target)
{
    int HitValue = 0;
    for (int i = 0; i < AttackTime; i++) {
        HitValue = (rand() + time(0)) % player.getMaxAttackPower()* PlayerAttackFac +1;
        if ((rand() + time(0)) % 100 + 1 < CritChance) {
            HitValue = HitValue * CritFac;
        }
        target.GetsHit(HitValue);
    }
}

GuardMove::GuardMove(string name) : Move(name)
{
    Name = name;
}

void GuardMove::Guard(Player player)
{
    player.setGuarding(true);
}

HealMove::HealMove(string name, int playerHealFac) : Move(name)
{
    Name = name;
    PlayerHealFac = playerHealFac;
}

void HealMove::Heal(Player player)
{
    int healAmount = (rand() + time(0)) % player.getMaxHealAmount() * PlayerHealFac + 1;
    player.Heal(healAmount);
}