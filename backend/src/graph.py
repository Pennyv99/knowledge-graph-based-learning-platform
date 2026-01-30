from email.errors import StartBoundaryNotFoundDefect
from platform import node
from tracemalloc import start
from neo4j import GraphDatabase, basic_auth
import json


class GraphDB:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=basic_auth(user, password))

    def close(self):
        self.driver.close()

    def search_node(self, id):
        query_str = 'MATCH (n) where id(n)=$id RETURN n as node'
        params = {
            'id': id
        }
        with self.driver.session() as session:
            result = session.read_transaction(lambda tx: list(tx.run(query_str, params)))
        res = [self.serialize_node(record['node']) for record in result]
        return res

    def search_graph(self, data):
        query_str = "match p = (n) -- (m) where n.name Contains $data return p as p"
        params = {
            'data': data
        }
        nodeset = []
        nodes = []
        links = []
        try:
            with self.driver.session() as session:
                result = session.read_transaction(lambda tx: list(tx.run(query_str, params)))
            # print(result.data())
            for path in result:
                # print(path['p'].Relationship)
                for item in path['p']:
                    # print(item.type)
                    start = self.serialize_node(item.nodes[0])
                    end = self.serialize_node(item.nodes[1])
                    # print(start['id'])
                    # print(start, end)
                    link = self.serialize_path(item)

                    # 结点去重
                    try:
                        nodeset.index(start['id'])
                    except Exception:
                        nodeset.append(start['id'])
                        nodes.append(start)

                    try:
                        nodeset.index(end['id'])
                    except Exception:
                        nodeset.append(end['id'])
                        nodes.append(end)

                    links.append(link)
            return links, nodes
        except Exception as e:
            print('Error!', e)
            links = []
            nodes = []
            return links, nodes

    def search_conc(self, id):
        # 根据结点属性查询相关联所有关系和结点
        print(id)
        # str = "MATCH (c:Concept) where c.id = $id OPTIONAL MATCH (c)<--(s:Subject) OPTIONAL MATCH (c) -->(o:Operation) RETURN s,c,o"
        str = "MATCH (c) where id(c)=$id RETURN id(c) as id , c.name as name "
        rel = "MATCH P=(c) -[r]-> () where id(c)=$id RETURN P"
        query_str = 'MATCH P=(c:Concept) --> (o) where id(c)=$id RETURN o.name as name, id(o) as id'
        params = {
            'id': id
        }
        with self.driver.session() as session:
            res = session.read_transaction(lambda tx: list(tx.run(query_str, params)))
            rel = session.read_transaction(lambda tx: list(tx.run(query_str, params)))
            node = session.read_transaction(lambda tx: list(tx.run(str, params)))
        return res, rel, node

    def get_course_structure(self, course_id):
        query_str = """
        MATCH (c:课程)-[r1:包括]->(s:章节)
        WHERE ID(c) = $course_id
        OPTIONAL MATCH (s)-[r2:包括]->(ss:节)
        OPTIONAL MATCH (ss)-[r3:包括]->(sss:小节)
        RETURN collect(distinct c) + collect(distinct s) + collect(distinct ss) + collect(distinct sss) AS Entities,
               collect(distinct r1) + collect(distinct r2) + collect(distinct r3) AS Relationships
        """
        params = {'course_id': course_id}
        with self.driver.session() as session:
            result = session.read_transaction(lambda tx: list(tx.run(query_str, params)))
        entities = []
        relationships = []
        if result:
            record = result[0]  # Assume only one record is returned
            entities = [self.serialize_node(node) for node in record['Entities'] if node is not None]
            entities = sorted(entities, key=lambda node: node['id'])
            relationships = [self.serialize_relationship(rel) for rel in record['Relationships'] if rel is not None]
        return entities, relationships

    def get_node_structure(self, node_id):
        query_str = """
        MATCH (start)
        WHERE ID(start) = $node_id
        OPTIONAL MATCH path=(start)-[:包括*]->(connectedNode)
        WITH start, NODES(path) AS nodes, RELATIONSHIPS(path) AS relationships
        UNWIND nodes + [start] AS all_nodes  // Ensure start node is always included
        UNWIND relationships AS all_relationships  // Handle potentially empty relationships
        RETURN COLLECT(DISTINCT all_nodes) AS Entities, 
               COLLECT(DISTINCT all_relationships) AS Relationships
        """
        params = {'node_id': node_id}
        with self.driver.session() as session:
            result = session.read_transaction(lambda tx: list(tx.run(query_str, params)))
        entities = []
        relationships = []
        if result:
            record = result[0]  # Assume only one record is returned
            entities = [self.serialize_node(node) for node in record['Entities'] if node is not None]
            entities = sorted(entities, key=lambda node: node['id'])
            relationships = [self.serialize_relationship(rel) for rel in record['Relationships'] if rel is not None]
        return entities, relationships

    def get_all_courses_structure(self):
        query_str = """
        MATCH (n)-[r]->(m)
        RETURN collect(distinct n) AS Nodes, collect(distinct r) AS Relationships
        """
        with self.driver.session() as session:
            result = session.read_transaction(lambda tx: list(tx.run(query_str)))
            if result:
                record = result[0]  # 假设只有一个记录返回
                nodes = [self.serialize_node(node) for node in record['Nodes']]
                relationships = [self.serialize_relationship(rel) for rel in record['Relationships']]
                return nodes, relationships
            else:
                return [], []

    def get_all_courses(self):
        query_str = """
        MATCH (n:`课程`) 
        RETURN collect(distinct n) AS Nodes
        """
        with self.driver.session() as session:
            result = session.read_transaction(lambda tx: list(tx.run(query_str)))
            if result:
                record = result[0]  # 假设只有一个记录返回
                nodes = [self.serialize_node(node) for node in record['Nodes']]

                return nodes
            else:
                return []

    # def get_major_courses_list(self, major_name):
    #     query_str = """
    #     MATCH (s:学科 {name: $major_name})-[:包括]->(c:课程)
    #     RETURN  collect(c.name) AS 课程列表
    #     """
    #     print(major_name)
    #     with self.driver.session() as session:
    #         # 执行读取事务，运行参数化的 Cypher 查询
    #         # result = session.read_transaction(lambda tx: tx.run(query_str, major_name=str(major_name)).data())
    #         result = session.read_transaction(lambda tx: tx.run(query_str, major_name=str(major_name)))
    #         print(result)
    #         if result:
    #             # 假定查询至少返回一条记录
    #             record = result[0]  # 获取第一条记录
    #             # 直接从记录中提取课程列表
    #             courses = record['课程列表']  # 课程名列表
    #             print("kecheng")
    #             print(courses)
    #             return courses
    #         else:
    #             return []
    def get_major_courses_list(self, major_name):
        query_str = """
        MATCH (s:学科 {name: $major_name})-[:包括]->(c:课程)
        RETURN collect(c.name) AS 课程列表
        """
        # print(f"Querying for major: {major_name}")  # 打印即将查询的学科名

        with self.driver.session() as session:
            # 执行读取事务，运行参数化的 Cypher 查询
            result = session.read_transaction(lambda tx: tx.run(query_str, major_name=major_name).data())
            # print("Result from database:", result)  # 打印数据库返回的原始结果

            if result:
                record = result[0]  # 获取第一条记录
                courses = record['课程列表']  # 课程名列表
                # print("Courses found:", courses)  # 打印找到的课程列表
                return courses
            else:
                # print("No courses found for the major.")  # 如果没有结果，打印这条消息
                return []

    def get_all_majors(self):
        query_str = """
        MATCH (n:`学科`) 
        RETURN collect(distinct n) AS Nodes
        """
        with self.driver.session() as session:
            result = session.read_transaction(lambda tx: list(tx.run(query_str)))
            if result:
                record = result[0]  # 假设只有一个记录返回
                nodes = [self.serialize_node(node) for node in record['Nodes']]

                return nodes
            else:
                return []

    def serialize_node(self, node):
        # Assuming the node has properties 'id', 'name', and possibly others
        return {
            'id': str(node.id),
            # 'id': node.id,
            'label': list(node.labels)[0],
            'properties': dict(node)
        }

    def serialize_relationship(self, relationship):
        # Assuming the relationship has a type and possibly properties

        return {

            'source': str(relationship.start_node.id),
            'target': str(relationship.end_node.id),
            'type': relationship.type
        }
