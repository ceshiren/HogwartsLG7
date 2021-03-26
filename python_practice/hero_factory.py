from python_practice.ez import EZ
from python_practice.jinx import Jinx


class HeroFactory:
    """
    简单工厂模式专门定义一个类来负责创建其他类型的英雄的实例
    """
    # 1. 职责清晰
    # 2. 提供了一个入口。比如添加了新的英雄，其他研发调用代码的过程中，可以以factory为主，
    # 不需要一个文件一个文件去读写的内容。
    def create_hero(self, name):
        if name == "Jinx":
            # ctrl/command 加鼠标左键
            return Jinx()
        elif name == "EZ":
            return EZ()
        else:
            raise Exception("此英雄不再英雄工厂中")

hero_factory = HeroFactory()
jinx = hero_factory.create_hero("Jinx")
ez = hero_factory.create_hero("EZ")
police = hero_factory.create_hero("police")

# jinx.fight(ez.hp, ez.power)