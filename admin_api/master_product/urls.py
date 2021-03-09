from django.urls import path
from .master_product_views import *

urlpatterns = [
    path('', AllMasterProductView.as_view(), name="fetch_all_master_products"),
    path('fetch/<str:master_product_id>', GetMasterProductView.as_view(), name="fetch_master_product_by_id"),
    path('create', CreateMasterProductView.as_view(), name="create_master_product"),
    path('update/<str:master_product_id>', UpdateMasterProductView.as_view(), name="update_master_product"),
    path('delete/<str:master_product_id>', DeleteMasterProductView.as_view(), name="delete_master_product"),
    path('search/<str:query>', SearchMasterProductView.as_view(), name="search_master_product"),
]