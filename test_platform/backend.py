import json
import logging

from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

# 实例化一个flask服务
app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)


# 路由 /根路由
@app.route('/')
def hello_world():
    return 'Hello, from wenzi!'


@app.route('/hello', methods=['GET', 'POST'])
def hello_world2():
    # 如果请求的方法是get
    if request.method == "GET":
        return f'Hello, get from {request.args.get("name", "hogwarts")}!'
    # 如果请求的方法是post
    elif request.method == "POST":
        return f'Hello, post from {request.json.get("name", "hogwarts")}!'
    else:
        return 'Hello, world!'


testcases = []
api = Api(app)


class TestCaseList:

    def __init__(self, name, description, steps):
        self.name = name
        self.description = description
        self.steps = steps

    def as_dict(self):
        return {"name": self.name, "description": self.description, "steps": self.steps}


# 类继承resoure
class TestCaseServer(Resource):
    # 如果是get请求，认为是去查询所有case
    def get(self):
        app.logger.info(request.args)
        return testcases

    # 如果是get请求，认为是去新增case
    def post(self):
        app.logger.info(request.args)
        app.logger.info(request.json)
        # 通过接口发送的数据进行TestCaseList类的实例化
        testcase = TestCaseList(**request.json)
        # 将testcase实例中的steps字段转为json字符串
        testcase.steps = json.dumps(request.json.get("steps"))
        app.logger.info(testcase)
        # 调用实例的as_dict方法   转换成字典后添加到列表
        testcases.append(testcase.as_dict())
        return {
            "error": 0,
            "msg": "OK"
        }


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:0208@localhost:3306/blog?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class TestCase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False)
    description = db.Column(db.String(80), unique=False, nullable=False)
    steps = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class TestCaseServerORM(Resource):
    # 如果是get请求，认为是去查询所有case
    def get(self):
        app.logger.info(request.args)
        case_id = request.args.get("id")
        if case_id:
            case_data = TestCase.query.filter_by(id=case_id).first()
            testcases = [case_data.as_dict()]
        else:
            case_data = TestCase.query.all()
            testcases = [i.as_dict() for i in case_data]
        return testcases

    # 如果是get请求，认为是去新增case
    def post(self):
        app.logger.info(request.args)
        app.logger.info(request.json)
        # 通过接口发送的数据进行TestCaseList类的实例化
        try:
            testcase = TestCase(**request.json)
            testcase.steps = json.dumps(request.json.get("steps"))
            app.logger.info(testcase)
            db.session.add(testcase)
            db.session.commit()
            db.session.close()
            return {
                "error": 0,
                "msg": "OK"
            }
        except:
            return {
                "error": 500,
                "msg": "server has an error!"
            }


# 注册到flask_restful api中去
api.add_resource(TestCaseServer, '/testcase')
api.add_resource(TestCaseServerORM, '/testcase_orm')

if __name__ == '__main__':
    # db.drop_all()
    db.create_all()
    app.run(debug=True, use_reloader=True)
