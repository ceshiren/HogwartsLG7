from test_requests.src.member_charge import MemberCharge


class TestMemberCharge:
    def setup(self):
        self.member = MemberCharge()

    def test_add(self):
        # 手机号已经存在
        self.member.add()
        r = self.member.add()
        assert r.get('errcode') == 60104

    def test_delete(self):
        r = self.member.delete()
        print(r)

    def test_update(self):
        r = self.member.update()
        print(r)

    def test_find(self):
        r = self.member.find()
        print(r)


class A:
    def a(self):
        print("a")
    # 加入了 staticmethod 装饰器就是静态方法
    # 在调用时候，可以直接调用，不需要初始化类
    @staticmethod
    def b():
        print("b")

def test_a():
    A().a()
    # 静态方法在调用时候，不需要初始化，直接调用即可
    A.b()
