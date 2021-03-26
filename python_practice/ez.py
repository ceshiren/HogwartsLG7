"""
一个回合制游戏，有两个英雄，分别以两个类进行定义。分别是EZ 和Jinx。
每个英雄都有 hp 属性和 power属性，hp 代表血量，power 代表攻击力
Jinx：hp 的初始值为 1000，power 的初始值为 210。
EZ：hp 的初始值为 1100，power 的初始值为 190。
每个英雄都有一个 fight 方法：
my_hp = hp - enemy_power
enemy_final_hp = enemy_hp - my_power
两个 hp 进行对比，血量剩余多的人获胜
"""
from python_practice.hero import Hero

class EZ(Hero):
    hp = 3100
    power = 190
    name = "EZ"
