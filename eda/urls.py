# eda/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('salesdata/', views.SalesDataList.as_view(), name='salesdata'),
    path('sales-by-year/', views.sales_value_by_year),
    path('volume-by-year/', views.volume_by_year),
    path('monthly-sales/<int:year>/', views.monthly_sales_trend),
    path('market-share/', views.market_share),
]
