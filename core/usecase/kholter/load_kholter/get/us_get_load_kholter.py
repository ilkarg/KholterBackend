from rest_framework.response import Response
from modules.module_kholter.orm.model.kholter.requests.request_get_kholter import RequestGetKholter
from modules.module_kholter.orm.model.kholter.kholter_serializer import KholterSerializer

class UsGetLoadKholter:
    def execute(request):
        return Response(RequestGetKholter.execute())
