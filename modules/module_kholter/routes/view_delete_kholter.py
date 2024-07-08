from rest_framework.views import APIView
from core.usecase.kholter.delete_kholter.delete.us_delete_delete_kholter import UsDeleteDeleteKholter

class ViewDeleteKholter(APIView):
    def delete(self, request, id):
        return UsDeleteDeleteKholter.execute(request, id)
