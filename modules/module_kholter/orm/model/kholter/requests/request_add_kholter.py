from modules.module_kholter.orm.model.kholter.kholter import Kholter

class RequestAddKholter:
    def execute(start_time, end_time, about):
        kholter = Kholter(start_time=start_time, end_time=end_time, about=about)
        kholter.save()
        return kholter
