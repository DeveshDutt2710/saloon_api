from rest_framework.views import APIView
from rest_framework import status as status_codes
from django.http import JsonResponse
from ..models import Profiles
from .product_impl import ProductImpl


class AllProductsView(APIView):

    def get(self, request, *args, **kwargs):
        query_params = request.query_params

        page_no = query_params.get('page', 1)
        page_size = query_params.get("page_size", 10)

        product_manager = ProductImpl(page=page_no, page_size=page_size)
        response = product_manager.fetch_all_products()

        return JsonResponse(response, status=status_codes.HTTP_200_OK)


class GetProductView(APIView):

    def get(self, request, product_id, *args, **kwargs):

        product_manager = ProductImpl(product_id)
        response = product_manager.fetch_product_by_id()

        return JsonResponse(response, status=status_codes.HTTP_200_OK)


class CreateProductView(APIView):

    def post(self, request, *args, **kwargs):

        product_manager = ProductImpl()
        response = product_manager.create_product(request.data)

        return JsonResponse(response, status=status_codes.HTTP_200_OK)


class UpdateProductView(APIView):

    def post(self, request, product_id, *args, **kwargs):

        product_manager = ProductImpl(product_id)
        response = product_manager.update_product(request.data)

        return JsonResponse(response, status=status_codes.HTTP_200_OK)


class DeleteProductView(APIView):

    def post(self, request, product_id, *args, **kwargs):

        product_manager = ProductImpl(product_id)
        response = product_manager.delete_product()

        return JsonResponse(response, status=status_codes.HTTP_200_OK)


class SearchProductView(APIView):

    def post(self, request, query, *args, **kwargs):
        query_params = request.query_params

        page_no = query_params.get('page', 1)
        page_size = query_params.get("page_size", 10)

        product_manager = ProductImpl(page=page_no, page_size=page_size)
        response = product_manager.search_product(query)

        return JsonResponse(response, status=status_codes.HTTP_200_OK)
