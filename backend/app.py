from flask import Flask,request,g,Response,send_from_directory
from flask_cors import CORS
from src.graph import GraphDB
from src import question_solve
import json
from json import dumps

url = 'bolt://39.105.221.59:7687'
username = 'neo4j'
password = '12345678'



# app = Flask(__name__, template_folder='../CSKG-frontend', static_folder='../CSKG-frontend', static_url_path='')
app = Flask(__name__, static_url_path='')
# app = Flask(__name__, static_folder='./static',static_url_path='')
CORS(app)
# apiPrefix = '/api/v1/'
apiPrefix = '/zhxh/'

@app.route('/')
def get_index():
    return 'hello'
    # return app.send_static_file('index.html')


@app.route(apiPrefix +'course', methods=['GET'])
def get_course_structure():
    # 尝试获取课程ID，如果未提供ID，则返回错误
    course_id = request.args.get('id', type=int)  # 不再默认为0，而是当没有id时返回None
    db = GraphDB(url, username, password)
    if course_id is None:

        entities, relationships = db.get_all_courses_structure()

    else:

        entities, relationships = db.get_course_structure(course_id)

    # 构造返回的JSON数据
    response_data = {
        'nodes': entities,
        'links': relationships
    }

    # 返回JSON响应
    return Response(json.dumps(response_data), mimetype='application/json')

@app.route(apiPrefix +'node', methods=['GET'])
def get_node_structure():
    # 尝试获取ID，如果未提供ID，则返回错误
    course_id = request.args.get('id', type=int)  # 不再默认为0，而是当没有id时返回None
    db = GraphDB(url, username, password)
    if course_id is None:
        entities, relationships = [],[]
    else:
        entities, relationships = db.get_node_structure(course_id)

    # 构造返回的JSON数据
    response_data = {
        'nodes': entities,
        'links': relationships
    }
    # 返回JSON响应
    return Response(json.dumps(response_data), mimetype='application/json')

#请求所有课程
@app.route(apiPrefix +'courses', methods=['GET'])
def get_all_courses():
    db = GraphDB(url, username, password)
    entities = db.get_all_courses()
    # 构造返回的JSON数据
    response_data = {
        'nodes': entities
    }
    # 返回JSON响应
    return Response(json.dumps(response_data), mimetype='application/json')

#请求所有专业
@app.route(apiPrefix +'majors', methods=['GET'])
def get_all_majors():
    db = GraphDB(url, username, password)
    entities = db.get_all_majors()
    # 构造返回的JSON数据
    response_data = {
        'nodes': entities
    }
    # 返回JSON响应
    return Response(json.dumps(response_data), mimetype='application/json')


# entity search
@app.route( apiPrefix + 'search', methods=['POST'])
def get_search():
    data = request.get_data(as_text = True)
    new_data = data.replace('"','')
    print('获取数据:', new_data)
    # res = {
    #     'code': 0,
    #     'data': data,
    #     'message': '测试数据'
    # }
    db = GraphDB(url,username,password)
    links,nodes = db.search_graph(new_data)
    db.close()
    # return res
    return Response(dumps({"nodes": nodes, 'links': links}),
                    mimetype="application/json")



@app.route( apiPrefix + '/question', methods=['POST'])
def query():
    data = request.get_data(as_text = True)
    print(data)

    if data:
        answer= question_solve.Solve().query(data)

    else:
        answer = "Sorry, I can't understand what you say."

    print(answer)
    return Response(dumps({"answer": answer}),
                    mimetype="application/json")

@app.route( apiPrefix + '/precourse', methods=['POST'])
def get_precourse():
    # 获取 JSON 格式的数据
    data = request.get_json()  # 使用 get_json() 直接解析 JSON 数据

    if data:
        # 从数据中获取具体的参数
        major = data.get('major', '')
        time = data.get('time', '')
        course = data.get('course', '')

        # 假设 question_solve.Solve().query(data) 能处理这些数据并返回结果
        precourse = question_solve.Solve().get_precourse(major,time,course)
    else:
        precourse = []

    # 输出到控制台，以便调试
    print("Received:", data)


    return Response(dumps({"precourse": precourse}),
                    mimetype="application/json")

@app.route( apiPrefix + '/path', methods=['POST'])
def get_lerning_path():
    # 获取 JSON 格式的数据
    data = request.get_json()  # 使用 get_json() 直接解析 JSON 数据

    if data:
        # 从数据中获取具体的参数
        precourse_list = data['precourse']
        major = data.get('major', '')
        time = data.get('time', '')
        course = data.get('course', '')
        # 假设 question_solve.Solve().query(data) 能处理这些数据并返回结果
        list_time,list_class,list_knowledge = question_solve.Solve().get_learning_path(major,time,course,precourse_list)
    else:
        list_time=[]
        list_class=[]
        list_knowledge=[]


    return Response(dumps({"time": list_time, "course": list_class,"knowledge":list_knowledge}),
                    mimetype="application/json")



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug = True)