import requests

from test_requests.src.base import Base


class MemberCharge(Base):
    def add(self):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}'
        data = {
            "userid": "zhangsan123",
            "name": "张三",
            "mobile": "+86 13800000000",
            "department": [1]}
        # json 代表把数据转为 json 进行发送
        # data -> 不是 json
        r = requests.post(url, json=data)
        return r.json()

    def delete(self):
        userid = "zhangsan123"
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={userid}'
        r = requests.get(url)
        return r.json()

    def update(self):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}'
        data = {
            "userid": "zhangsan123",
            "name": "李四123"
        }
        r = requests.post(url, json=data)
        return r.json()

    def find(self):
        userid = "zhangsan123"
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={userid}'
        r = requests.get(url)
        return r.json()
