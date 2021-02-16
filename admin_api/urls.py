from django.urls import path, include

urlpatterns = [
    path('profiles/', include('admin_api.profiles.urls')),
    path('products/', include('admin_api.products.urls')),
    path('enquiries/', include('admin_api.enquiries.urls')),
    path('coupons/', include('admin_api.coupons.urls')),
    path('orders/', include('admin_api.orders.urls')),
]
