from rest_framework.response import Response
from modules.module_kholter.orm.model.kholter.requests.request_delete_kholter import RequestDeleteKholter
from modules.module_kholter.orm.model.kholter.kholter_serializer import KholterSerializer

class UsDeleteDeleteKholter:
    def execute(request, id):
        if RequestDeleteKholter.execute(id=id):
            return Response({'response': 'Запись успешно удалена'})
        else:
            return Response({'response': 'Во время удаления записи что-то пошло не так'})
