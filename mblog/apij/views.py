import os
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def load_json_view(request):
    # 获取JSON文件路径
    json_file_path = os.path.join(os.path.dirname(__file__), 'static/package.json')

    # 读取JSON文件
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    # 返回JSON响应
    return Response(data)