from django.urls import path
from .coupon_views import *

urlpatterns = [
    path('', AllCouponView.as_view(), name="fetch_all_coupons"),
    path('fetch/<str:coupon_id>', GetCouponView.as_view(), name="fetch_coupon_by_id"),
    path('create', CreateCouponView.as_view(), name="create_coupon"),
    path('update/<str:coupon_id>', UpdateCouponView.as_view(), name="update_coupon"),
    path('delete/<str:coupon_id>', DeleteCouponView.as_view(), name="delete_coupon"),
    path('search/<str:query>', SearchCouponView.as_view(), name="search_coupon"),
]
