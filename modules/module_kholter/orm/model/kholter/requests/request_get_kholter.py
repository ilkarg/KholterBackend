from modules.module_kholter.orm.model.kholter.kholter import Kholter

class RequestGetKholter:
    def execute():
        return Kholter.objects.values()
