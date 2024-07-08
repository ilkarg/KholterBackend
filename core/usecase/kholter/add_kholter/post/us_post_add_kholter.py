from rest_framework.response import Response
from modules.module_kholter.orm.model.kholter.requests.request_add_kholter import RequestAddKholter
from modules.module_kholter.orm.model.kholter.kholter_serializer import KholterSerializer

class UsPostAddKholter:
    def execute(request):
        kholter = RequestAddKholter.execute(start_time=request.data.get('start_time'), end_time=request.data.get('end_time'), about=request.data.get('about'))
        kholter_serialized = KholterSerializer(kholter)
        return Response({'id': kholter_serialized.data['id'], 'start_time': kholter_serialized.data['start_time'], 'end_time': kholter_serialized.data['end_time'], 'about': kholter_serialized.data['about']})
