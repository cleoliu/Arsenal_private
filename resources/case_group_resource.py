from flask import jsonify, request
from flask_restful import Resource, reqparse


class Labels(Resource):

    def get(self):
        datas = [
            {
                'label_id': 'hash1',
                'label_name': 'P0',
                'color': '#0066aa'
            },
            {
                'label_id': 'hash2',
                'label_name': 'P1',
                'color': '#0066aa'
            },
        ]

        return jsonify(datas)


class Sections(Resource):

    def get(self):
        datas = [
            {
                'text': "Root",
                'section_id': 'hash1',
                'expanded': True,
                "items": [
                    {
                        "text": "Section1",
                        'section_id': 'hash2',
                        'expanded': True,
                        "items": [
                            {"text": "Section1-1",
                             'section_id': 'hash3','expanded': False},
                        ]
                    },
                    {"text": "Section2", 'section_id': 'hash4', 'expanded': False,},
                    {"text": "Section3", 'section_id': 'hash5','expanded': False}
                ]
            },
        ]

        return jsonify(datas)



class CasesbyGroup(Resource):

    def __init__(self):
        print("CCCCC")

    def get(self):
        print(request.json)
        print("DDDDD")

        parser = reqparse.RequestParser()
        print("EEEE")
        parser.add_argument('group_id', type=str, required=True)
        print("FFF")
        parser_result = parser.parse_args()
        print("123123")
        print(parser_result)
        group_name = parser_result.get('group_id')
        print(group_name)
        if not group_name:
            return []
        datas = [
            {
                'sections_id': 'hash1',
                'sections_name': 'root',
                'case_list': [
                    {
                        'case_id': 'case_id_0',
                        'title': 'case 0',
                        'assignee': 'fabian lin',
                        'create_date': '2022/02/03 16:45:12',
                        'sections_id': 'hash1',
                        'sections_name': 'root',
                        'labels': [
                            {
                                'label_name': 'P0',
                                'color': '#5F9CC6'
                            }, {
                                'label_name': 'BAT',
                                'color': '#FD6D6D'
                            }, {
                                'label_name': 'Regression',
                                'color': '#5FC6B3'
                            },
                        ]

                    },
                    {
                        'case_id': 'case_id_2',
                        'title': 'case 2',
                        'assignee': 'fabian lin',
                        'create_date': '2022/02/03 16:45:12',
                        'sections_id': 'hash1',
                        'sections_name': 'root',
                        'labels': [
                            {
                                'label_name': 'P0',
                                'color': '#5F9CC6'
                            }, {
                                'label_name': 'BAT',
                                'color': '#FD6D6D'
                            },
                        ]

                    }
                ]
            },
            {
                'sections_id': 'hash2',
                'sections_name': 'Section1',
                'case_list': [
                    {
                        'case_id': 'case_id_1',
                        'title': 'case 1',
                        'assignee': 'fabian lin',
                        'create_date': '2022/02/03 16:45:12',
                        'sections_id': 'hash2',
                        'sections_name': 'Section1',
                        'labels': [
                            {
                                'label_name': 'P0',
                                'color': '#5F9CC6'
                            },{
                                'label_name': 'BAT',
                                'color': '#FD6D6D'
                            },
                        ]

                    }
                ]
            }
        ]

        return jsonify(datas)



class CaseGroups(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('group_name', required=True)

    def get(self):
        data = [
            {
                "group_id": "hash1",
                "group_name": "測試",
                "sections": 10,
                "cases": 666,
                'description': 'sadafdsaf  addjahsgd asdkjadsf as;lkfj asdfl;k adsflkjfasdfuiytasdjhbf asduyifgasdjhgf iuayshdgbfmnsbadvfkuyasdgf',
            },
            {
                "group_id": "hash2",
                "group_name": "回歸測試",
                "sections": 10,
                "cases": 666,
                'description': 'sadafdsaf  addjahsgd asdkjadsf as;lkfj asdfl;k adsflkjfasdfuiytasdjhbf asduyifgasdjhgf iuayshdgbfmnsbadvfkuyasdgf',
            },
            {
                "group_id": "hash3",
                "group_name": "新功能測試",
                "sections": 10,
                "cases": 666,
                'description': 'sadafdsaf  addjahsgd asdkjadsf as;lkfj asdfl;k adsflkjfasdfuiytasdjhbf asduyifgasdjhgf iuayshdgbfmnsbadvfkuyasdgf',
            },
            {
                "group_id": "hash4",
                "group_name": "驗收測試",
                "sections": 10,
                "cases": 666,
                'description': 'sadafdsaf  addjahsgd asdkjadsf as;lkfj asdfl;k adsflkjfasdfuiytasdjhbf asduyifgasdjhgf iuayshdgbfmnsbadvfkuyasdgf',
            },
            {
                "group_id": "hash5",
                "group_name": "效能測試",
                "sections": 10,
                "cases": 666,
                'description': 'sadafdsaf  addjahsgd asdkjadsf as;lkfj asdfl;k adsflkjfasdfuiytasdjhbf asduyifgasdjhgf iuayshdgbfmnsbadvfkuyasdgf',
            },
        ]
        return jsonify(data)

    def post(self):
        arg = self.parser.parse_args()
        print('****----')
        print(arg)
        return arg
