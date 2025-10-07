# eda/views.py
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import SalesData
from .serializers import SalesDataSerializer
from django.db.models import Sum

# List & Filter
class SalesDataList(generics.ListAPIView):
    serializer_class = SalesDataSerializer

    def get_queryset(self):
        queryset = SalesData.objects.all()
        filters = self.request.query_params

        for field in ['brand','pack_type','ppg','channel','year','region','category','sub_category']:
            value = filters.get(field)
            if value:
                queryset = queryset.filter(**{field: value})

        return queryset

# Aggregated Endpoints for Charts
@api_view(['GET'])
def sales_value_by_year(request):
    data = SalesData.objects.values('year').annotate(sales=Sum('sales_value')).order_by('year')
    return Response(data)

@api_view(['GET'])
def volume_by_year(request):
    data = SalesData.objects.values('year').annotate(volume=Sum('volume')).order_by('year')
    return Response(data)

@api_view(['GET'])
def monthly_sales_trend(request, year):
    data = SalesData.objects.filter(year=year).values('month').annotate(sales=Sum('sales_value')).order_by('month')
    return Response(data)

@api_view(['GET'])
def market_share(request):
    data = SalesData.objects.values('brand').annotate(sales=Sum('sales_value'), volume=Sum('volume')).order_by('-sales')
    return Response(data)
