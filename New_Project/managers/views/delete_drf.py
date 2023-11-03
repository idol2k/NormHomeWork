from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import ModelSerializer


class DeleteView(APIView):
    def delete(self, request, pk):
        try:
            instance = ModelSerializer.objects.get(pk=pk)
        except ModelSerializer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)