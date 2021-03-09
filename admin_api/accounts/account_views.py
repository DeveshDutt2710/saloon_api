from rest_framework.views import APIView
from rest_framework import status as status_codes
from django.http import JsonResponse
from ..models import Profiles
from .account_impl import AccountImpl


class AllAccountView(APIView):

    def get(self, request, *args, **kwargs):

        query_params = request.query_params

        page_no = query_params.get('page', 1)
        page_size = query_params.get("page_size", 10)

        account_manager = AccountImpl(page=page_no, page_size=page_size)
        response = account_manager.fetch_all_accounts()

        return JsonResponse(response, status=status_codes.HTTP_200_OK)


class GetAccountView(APIView):

    def get(self, request, profile_id, *args, **kwargs):

        account_manager = AccountImpl(profile_id)
        response = account_manager.fetch_account_by_id()

        return JsonResponse(response, status=status_codes.HTTP_200_OK)


class CreateAccountView(APIView):

    def post(self, request, *args, **kwargs):

        account_manager = AccountImpl()
        response = account_manager.create_account(request.data)

        return JsonResponse(response, status=status_codes.HTTP_200_OK)


class UpdateAccountView(APIView):

    def post(self, request, profile_id, *args, **kwargs):

        account_manager = AccountImpl(profile_id)
        response = account_manager.update_account(request.data)

        return JsonResponse(response, status=status_codes.HTTP_200_OK)


class DeleteAccountView(APIView):

    def post(self, request, profile_id, *args, **kwargs):

        account_manager = AccountImpl(profile_id)
        response = account_manager.delete_account()

        return JsonResponse(response, status=status_codes.HTTP_200_OK)


class SearchAccountView(APIView):

    def post(self, request, query, *args, **kwargs):
        query_params = request.query_params

        page_no = query_params.get('page', 1)
        page_size = query_params.get("page_size", 10)

        account_manager = AccountImpl(page=page_no, page_size=page_size)
        response = account_manager.search_account(query)

        return JsonResponse(response, status=status_codes.HTTP_200_OK)
