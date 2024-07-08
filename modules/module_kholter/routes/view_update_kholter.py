from rest_framework.views import APIView
from core.usecase.kholter.update_kholter.put.us_put_update_kholter import UsPutUpdateKholter

class ViewUpdateKholter(APIView):
    def put(self, request):
        return UsPutUpdateKholter.execute(request)
