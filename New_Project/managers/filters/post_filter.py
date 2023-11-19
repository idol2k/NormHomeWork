from rest_framework import filters
from ..models import ModelSerializer

class ManageFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        age = request.query_params.get('age')
        if age:
            queryset = queryset.filter(age_get=age)
        return queryset