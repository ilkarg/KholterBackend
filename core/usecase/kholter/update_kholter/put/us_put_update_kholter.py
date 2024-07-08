from rest_framework.response import Response
from modules.module_kholter.orm.model.kholter.requests.request_update_kholter import RequestUpdateKholter
from modules.module_kholter.orm.model.kholter.kholter_serializer import KholterSerializer

class UsPutUpdateKholter:
    def execute(request):
        kholter = RequestUpdateKholter.execute(id=request.data.get('id'), start_time=request.data.get('start_time'), end_time=request.data.get('end_time'), about=request.data.get('about'))
        if kholter['status']:
            kholter_serialized = KholterSerializer(kholter['response'])
            return Response({'id': kholter_serialized.data['id'], 'start_time': kholter_serialized.data['start_time'], 'end_time': kholter_serialized.data['end_time'], 'about': kholter_serialized.data['about']})
        else:
            return Response({'response': kholter['response']})
