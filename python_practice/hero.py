class Hero:
    hp = 0
    power = 0
    name = ""

    def fight(self, enemy_hp, enemy_power):
        """
        两方进行一回合制的对打
        :param enemy_hp: 敌人的血量
        :param enemy_power:  敌人的攻击力
        :return:
        """
        # 我的血量
        # 通过实例变量的方式调用类变量
        final_hp = self.hp - enemy_power
        enemy_final_hp = enemy_hp - self.power
        if final_hp > enemy_final_hp:
            print(f"{self.name}赢了")
        elif final_hp < enemy_final_hp:
            print("敌人赢了")
        else:
            print("我们打平了")

