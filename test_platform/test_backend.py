import requests as requests


def test_backend_hello():
    url = "http://127.0.0.1:5000/hello"
    data = {"nam": "zhangsan"}
    rs = requests.post(url, json=data)
    print(rs.text)


def test_case_add():
    url = "http://127.0.0.1:5000/testcase"
    data = {
        "name": "testcase1", "description": "abcd", "steps": ["a", "b", "c"]
    }
    rs = requests.post(url, json=data)
    print(rs.json())


def test_case_add_orm():
    url = "http://127.0.0.1:5000/testcase_orm"
    data = {
        "name": "testcase1", "description": "abcd", "steps": ["a", "b", "c"]
    }
    rs = requests.post(url, json=data)
    print(rs.json())
