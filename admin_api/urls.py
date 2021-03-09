from django.urls import path, include

urlpatterns = [
    path('profiles/', include('admin_api.profiles.urls')),
    path('products/', include('admin_api.products.urls')),
    path('enquiries/', include('admin_api.enquiries.urls')),
    path('coupons/', include('admin_api.coupons.urls')),
    path('orders/', include('admin_api.orders.urls')),
    path('categories/', include('admin_api.categories.urls')),
    path('master_products/', include('admin_api.master_product.urls')),
    path('accounts/', include('admin_api.accounts.urls')),
]
