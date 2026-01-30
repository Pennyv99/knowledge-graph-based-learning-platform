import requests
import json
from src.graph import GraphDB
from platform import node
import os
import re

class Solve(object):
    def __init__(self):
        socket.setdefaulttimeout(500)
        # 设定模型服务的URL和端口
        self.api_url = 'http://localhost:8000'

    def query(self, question):
        data = {'prompt': question}
        response = send_data_to_model(api_url, data)
        if response:
            print("Model response:", response)
        else:
            print("Failed to get response from the model.")
        ans = response[0]["message"]["content"]

        print(ans)
        return ans

    def get_precourse(self, major,time,course):

        db = GraphDB(url, username, password)
        course_list=db.get_major_courses_list(major)
        str1 = "我是"
        str2 = "专业的学生，我想在"
        str3 = "之内学会"
        str4 = "课程，请给我推荐一个学习路线规划（学习该课程之前应该掌握的课程），推荐课程从以下内容中选择"
        str5 = "。要求返回数据格式为：学习路线：课程1,课程2,课程3...（如果与所学课程关系不大的课程请不要推荐，要求推荐课程足够简洁，学习路线的最后一个课程一定要是要学习的目标课程,只推荐课程名称，课程后面不要加()解释，不要有其他说明和解释）"
        prompt = str1 + major + str2 + time + str3 + course + str4 + str(course_list) + str5
        data = {'prompt': prompt}
        response = send_data_to_model(api_url, data)
        if response:
            print("Model response:", response)
        else:
            print("Failed to get response from the model.")
        path = response[0]["message"]["content"]
        path = path.replace('学习路线：', '').replace('课程', '')
        delimiter_pattern = r'(?<!\w)[\s,]+'
        precourselist = re.split(delimiter_pattern, path)
        # 使用 strip() 方法删除字符串前后的空格，并用 replace() 方法删除中间的空格
        precourselist = [course.strip().replace(" ", "") for course in precourselist]

        # print(precourselist)
        return precourselist

    def get_learning_path(self,major,time,course, course_list_back):

        str1 = "我是"
        str2 = "专业的学生，我想在"
        str3 = "之内学会"
        str4 = ("课程，我规划的学习路线如下：\n学习路线：")
        str5 = "\n请给出对应的学习计划表，用表格的方式呈现，表格的列名分别为学习阶段，学习课程，学习内容。（不要给表格外其余的说明）"

        prompt = str1+major+str2+time+ str3 +course+ str4+str(course_list_back) + str5
        data = {'prompt': prompt}
        response = send_data_to_model(api_url, data)
        if response:
            print("Model response:", response)
        else:
            print("Failed to get response from the model.")
        schedule = response[0]["message"]["content"]
        print(schedule)

        lines = schedule.strip().split('\n')
        table_lines = []
        advice_text = []
        table_started = False

        for line in lines:
            if "| 学习阶段 |" in line:  # 表格头部标记
                table_started = True
            if table_started:
                if line.strip() == "":  # 表格与建议文本之间的分界（空行）
                    table_started = False
                else:
                    table_lines.append(line)
            else:
                advice_text.append(line)

        # 解析表格内容
        list_time, list_class, list_knowledge = [], [], []
        for row in table_lines:
            columns = row.split('|')
            if len(columns) == 5:  # 完整的表格行有5个元素（包括两边的空白）
                list_time.append(columns[1].strip())
                list_class.append(columns[2].strip())
                list_knowledge.append(columns[3].strip())

        # 合并建议文本
        advice_text = ' '.join(advice_text).strip()

        del list_time[:2]
        del list_class[:2]
        del list_knowledge[:2]
        return list_time,list_class,list_knowledge


def send_data_to_model(api_url, data):
    """
    发送数据到模型API并接收响应。
    参数:
        api_url (str): 模型API的URL。
        data (dict): 要发送的数据。
    返回:
        dict: 模型的响应数据。
    """
    headers = {
        'Content-Type': 'application/json'
    }

    try:
        response = requests.post(api_url, headers=headers, json=data)
        response.raise_for_status()  # 检查响应是否成功
        return response.json()  # 返回JSON格式的响应数据
    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else", err)

    return None  # 如果出现错误，返回None


