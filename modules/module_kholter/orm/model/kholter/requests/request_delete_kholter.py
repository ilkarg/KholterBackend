from modules.module_kholter.orm.model.kholter.kholter import Kholter

class RequestDeleteKholter:
    def execute(id):
        return Kholter.objects.filter(id=id).delete()
