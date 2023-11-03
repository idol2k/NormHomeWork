from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from ..serializer import ManagersSerializer
from ..models import ModelSerializer


class ReadView(APIView):
    template_name = 'api.html'
    renderer_classes = [TemplateHTMLRenderer]
    def get(self, request):
        queryset = ModelSerializer.objects.all()
        serializer = ManagersSerializer(queryset, many=True)
        return Response(serializer.data)