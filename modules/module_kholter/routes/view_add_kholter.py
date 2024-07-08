from rest_framework.views import APIView
from core.usecase.kholter.add_kholter.post.us_post_add_kholter import UsPostAddKholter

class ViewAddKholter(APIView):
    def post(self, request):
        return UsPostAddKholter.execute(request)
