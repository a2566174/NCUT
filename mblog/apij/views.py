import os
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def load_json_view(request):
    # JSON文件路徑
    json_file_path = os.path.join(os.path.dirname(__file__), 'static/package.json')

    # 讀取JSON文件
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    # 返回JSON
    return Response(data)