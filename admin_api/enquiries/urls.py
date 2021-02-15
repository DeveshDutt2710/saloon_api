from django.urls import path
from .enquiry_views import (AllEnquiriesView, GetEnquiryView,
                            CreateEnquiryView, UpdateeEnquiryView,
                            DeleteEnquiryView, SearchEnquiryView)

urlpatterns = [
    path('', AllEnquiriesView.as_view(), name="fetch_all_enquiries"),
    path('fetch/<str:enquiry_id>', GetEnquiryView.as_view(), name="fetch_enquiry_by_id"),
    path('create', CreateEnquiryView.as_view(), name="create_enquiry"),
    path('update/<str:enquiry_id>', UpdateeEnquiryView.as_view(), name="update_enquiry"),
    path('delete/<str:enquiry_id>', DeleteEnquiryView.as_view(), name="delete_enquiry"),
    path('search/<str:query>', SearchEnquiryView.as_view(), name="search_enquiry"),
]
