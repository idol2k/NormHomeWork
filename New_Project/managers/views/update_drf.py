from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import ModelSerializer
from ..serializer import ManagersSerializer


class UpdateView(APIView):
    def put(self, request, pk):
        try:
            instance = ModelSerializer.objects.get(pk=pk)
        except ModelSerializer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ManagersSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)