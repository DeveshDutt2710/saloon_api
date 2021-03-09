from django.urls import path
from .account_views import (AllAccountView, GetAccountView,
                            CreateAccountView, UpdateAccountView,
                            DeleteAccountView, SearchAccountView)

urlpatterns = [
    path('', AllAccountView.as_view(), name="fetch_all_profiles"),
    path('fetch/<str:profile_id>', GetAccountView.as_view(), name="fetch_profile_by_id"),
    path('create', CreateAccountView.as_view(), name="create_profile"),
    path('update/<str:profile_id>', UpdateAccountView.as_view(), name="update_profile"),
    path('delete/<str:profile_id>', DeleteAccountView.as_view(), name="delete_profile"),
    path('search/<str:query>', SearchAccountView.as_view(), name="search_profile"),
]