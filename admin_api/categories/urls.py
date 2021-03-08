from django.urls import path
from .categories_views import *

urlpatterns = [
    path('', AllCategoriesView.as_view(), name="fetch_all_categories"),
    path('fetch/<str:category_id>', GetCategoryView.as_view(), name="fetch_category_by_id"),
    path('create', CreateCategoryView.as_view(), name="create_category"),
    path('update/<str:category_id>', UpdateCategoryView.as_view(), name="update_category"),
    path('delete/<str:category_id>', DeleteCategoryView.as_view(), name="delete_category"),
    path('search/<str:query>', SearchCategoryView.as_view(), name="search_category"),
]