from rest_framework.views import APIView
from rest_framework import status as status_codes
from django.http import JsonResponse
from .master_product_impl import MasterProductImpl


class AllMasterProductView(APIView):

    def get(self, request, *args, **kwargs):
        query_params = request.query_params

        page_no = query_params.get('page', 1)
        page_size = query_params.get("page_size", 10)

        master_product_manager = MasterProductImpl(page=page_no, page_size=page_size)
        response = master_product_manager.fetch_all_master_products()

        return JsonResponse(response, status=status_codes.HTTP_200_OK)


class GetMasterProductView(APIView):

    def get(self, request, master_product_id, *args, **kwargs):

        master_product_manager = MasterProductImpl(master_product_id)
        response = master_product_manager.fetch_master_product_by_id()

        return JsonResponse(response, status=status_codes.HTTP_200_OK)


class CreateMasterProductView(APIView):

    def post(self, request, *args, **kwargs):

        master_product_manager = MasterProductImpl()
        response = master_product_manager.create_master_product(request.data)

        return JsonResponse(response, status=status_codes.HTTP_200_OK)


class UpdateMasterProductView(APIView):

    def post(self, request, master_product_id, *args, **kwargs):

        master_product_manager = MasterProductImpl(master_product_id)
        response = master_product_manager.update_master_product(request.data)

        return JsonResponse(response, status=status_codes.HTTP_200_OK)


class DeleteMasterProductView(APIView):

    def post(self, request, master_product_id, *args, **kwargs):

        master_product_manager = MasterProductImpl(master_product_id)
        response = master_product_manager.delete_master_product()

        return JsonResponse(response, status=status_codes.HTTP_200_OK)


class SearchMasterProductView(APIView):

    def post(self, request, query, *args, **kwargs):
        query_params = request.query_params

        page_no = query_params.get('page', 1)
        page_size = query_params.get("page_size", 10)

        master_product_manager = MasterProductImpl(page=page_no, page_size=page_size)
        response = master_product_manager.search_master_product(query)

        return JsonResponse(response, status=status_codes.HTTP_200_OK)
