from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import *
from rest_framework import status


class Logs(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, id=None):
        if id:
            obj = Log.objects.get(id=id)
            serializer = LogSerializer(obj, many=False)
            return Response(serializer.data)
        else:
            objs = Log.objects.all()
            serializer = LogSerializer(objs, many=True)
            return Response(serializer.data)