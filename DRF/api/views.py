from rest_framework.views import APIView
from rest_framework.response import Response

class BasicApiView(APIView):
    def get(self,request):
        return Response({"message":"Welcome to Django DRF Project !"})