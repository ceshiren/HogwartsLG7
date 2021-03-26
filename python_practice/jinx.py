from python_practice.ez import EZ
from python_practice.hero import Hero


class Jinx(Hero):
    hp = 2000
    power = 210
    name = "Jinx"


jinx = Jinx()
# import 快捷键 alt +回车, mac对应option键位
ez = EZ()
# 如果是ez调用fight方法应该提醒，ez赢了
# ez.fight()
# 传入ez 的hp 和 攻击力
# 如果jinx 赢了， 那么要提示jinx 赢了
ez.fight(jinx.hp, jinx.power)
