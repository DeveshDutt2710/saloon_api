from rest_framework.views import APIView
from rest_framework import status as status_codes
from django.http import JsonResponse
from .categories_impl import CategoryImpl


class AllCategoriesView(APIView):

    def get(self, request, *args, **kwargs):
        query_params = request.query_params

        page_no = query_params.get('page', 1)
        page_size = query_params.get("page_size", 10)

        category_manager = CategoryImpl(page=page_no, page_size=page_size)
        response = category_manager.fetch_all_categories()

        return JsonResponse(response, status=status_codes.HTTP_200_OK)


class GetCategoryView(APIView):

    def get(self, request, category_id, *args, **kwargs):

        category_manager = CategoryImpl(category_id)
        response = category_manager.fetch_category_by_id()

        return JsonResponse(response, status=status_codes.HTTP_200_OK)


class CreateCategoryView(APIView):

    def post(self, request, *args, **kwargs):

        category_manager = CategoryImpl()
        response = category_manager.create_category(request.data)

        return JsonResponse(response, status=status_codes.HTTP_200_OK)


class UpdateCategoryView(APIView):

    def post(self, request, category_id, *args, **kwargs):

        category_manager = CategoryImpl(category_id)
        response = category_manager.update_category(request.data)

        return JsonResponse(response, status=status_codes.HTTP_200_OK)


class DeleteCategoryView(APIView):

    def post(self, request, category_id, *args, **kwargs):

        category_manager = CategoryImpl(category_id)
        response = category_manager.delete_category()

        return JsonResponse(response, status=status_codes.HTTP_200_OK)


class SearchCategoryView(APIView):

    def post(self, request, query, *args, **kwargs):
        query_params = request.query_params

        page_no = query_params.get('page', 1)
        page_size = query_params.get("page_size", 10)

        category_manager = CategoryImpl(page=page_no, page_size=page_size)
        response = category_manager.search_category(query)

        return JsonResponse(response, status=status_codes.HTTP_200_OK)
