from rest_framework.views import APIView
from rest_framework import status as status_codes
from django.http import JsonResponse
from .enquiry_impl import EnquiryImpl


class AllEnquiriesView(APIView):

    def get(self, request, *args, **kwargs):
        query_params = request.query_params

        page_no = query_params.get('page', 1)
        page_size = query_params.get("page_size", 10)

        enquiry_manager = EnquiryImpl(page=page_no, page_size=page_size)
        response = enquiry_manager.fetch_all_enquiries()

        return JsonResponse(response, status=status_codes.HTTP_200_OK)


class GetEnquiryView(APIView):

    def get(self, request, enquiry_id, *args, **kwargs):

        enquiry_manager = EnquiryImpl(enquiry_id)
        response = enquiry_manager.fetch_enquiry_by_id()

        return JsonResponse(response, status=status_codes.HTTP_200_OK)


class CreateEnquiryView(APIView):

    def post(self, request, *args, **kwargs):

        enquiry_manager = EnquiryImpl()
        response = enquiry_manager.create_enquiry(request.data)

        return JsonResponse(response, status=status_codes.HTTP_200_OK)


class UpdateeEnquiryView(APIView):

    def post(self, request, enquiry_id, *args, **kwargs):

        enquiry_manager = EnquiryImpl(enquiry_id)
        response = enquiry_manager.update_enquiry(request.data)

        return JsonResponse(response, status=status_codes.HTTP_200_OK)


class DeleteEnquiryView(APIView):

    def post(self, request, enquiry_id, *args, **kwargs):

        enquiry_manager = EnquiryImpl(enquiry_id)
        response = enquiry_manager.delete_enquiry()

        return JsonResponse(response, status=status_codes.HTTP_200_OK)


class SearchEnquiryView(APIView):

    def post(self, request, query, *args, **kwargs):
        query_params = request.query_params

        page_no = query_params.get('page', 1)
        page_size = query_params.get("page_size", 10)

        enquiry_manager = EnquiryImpl(page=page_no, page_size=page_size)
        response = enquiry_manager.search_enquiry(query)

        return JsonResponse(response, status=status_codes.HTTP_200_OK)
