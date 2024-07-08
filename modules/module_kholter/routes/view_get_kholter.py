from rest_framework.views import APIView
from core.usecase.kholter.load_kholter.get.us_get_load_kholter import UsGetLoadKholter

class ViewGetKholter(APIView):
    def get(self, request):
        return UsGetLoadKholter.execute(request)
