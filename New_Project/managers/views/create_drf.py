from rest_framework import filters
from rest_framework import pagination
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializer import ManagersSerializer
from ..models import ModelSerializer
from ..filters import ManageFilter

class ManagersPagination(pagination.PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'


class ManagersViewSerializer(APIView):
    def post(self, request):
        serializer = ManagersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors)

    def get(self, request):
        posts = ModelSerializer.objects.all()
        serializer = ManagersSerializer(posts, many=True)
        return Response(serializer.data)

class ViewModel(generics.RetrieveAPIView):
    queryset = ModelSerializer.objects.all()
    serializer_class = ManagersSerializer
    lookup_field = 'id'

class CreateView(generics.CreateAPIView):
    queryset = ModelSerializer.objects.all()
    serializer_class = ManagersSerializer

class ReadView(generics.ListAPIView):
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, ManageFilter]
    pagination_class = ManagersPagination

    queryset = ModelSerializer.objects.all()
    serializer_class = ManagersSerializer


class UpdateView(generics.UpdateAPIView):
    queryset = ModelSerializer.objects.all()
    serializer_class = ManagersSerializer


class DeleteView(generics.DestroyAPIView):
    queryset = ModelSerializer.objects.all()
    serializer_class = ManagersSerializer