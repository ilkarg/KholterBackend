from modules.module_kholter.orm.model.kholter.kholter import Kholter

class RequestUpdateKholter:
    def execute(id, start_time, end_time, about):
        try:
            kholter = Kholter.objects.get(id=id)

            kholter.start_time = start_time
            kholter.end_time = end_time
            kholter.about = about

            kholter.save()

            return {'status': True, 'response': kholter}
        except Kholter.DoesNotExist:
            return {'status': False, 'response': 'Во время обновления записи что-то пошло не так'}
