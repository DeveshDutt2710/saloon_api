from rest_framework.views import APIView
from rest_framework import status as status_codes
from django.http import JsonResponse
from .coupon_impl import CouponImpl


class AllCouponView(APIView):

    def get(self, request, *args, **kwargs):
        query_params = request.query_params

        page_no = query_params.get('page', 1)
        page_size = query_params.get("page_size", 10)

        coupon_manager = CouponImpl(page=page_no, page_size=page_size)
        response = coupon_manager.fetch_all_coupons()

        return JsonResponse(response, status=status_codes.HTTP_200_OK)


class GetCouponView(APIView):

    def get(self, request, coupon_id, *args, **kwargs):

        coupon_manager = CouponImpl(coupon_id)
        response = coupon_manager.fetch_coupon_by_id()

        return JsonResponse(response, status=status_codes.HTTP_200_OK)


class CreateCouponView(APIView):

    def post(self, request, *args, **kwargs):

        coupon_manager = CouponImpl()
        response = coupon_manager.create_coupon(request.data)

        return JsonResponse(response, status=status_codes.HTTP_200_OK)


class UpdateCouponView(APIView):

    def post(self, request, coupon_id, *args, **kwargs):

        coupon_manager = CouponImpl(coupon_id)
        response = coupon_manager.update_coupon(request.data)

        return JsonResponse(response, status=status_codes.HTTP_200_OK)


class DeleteCouponView(APIView):

    def post(self, request, coupon_id, *args, **kwargs):

        coupon_manager = CouponImpl(coupon_id)
        response = coupon_manager.delete_coupon()

        return JsonResponse(response, status=status_codes.HTTP_200_OK)


class SearchCouponView(APIView):

    def post(self, request, query, *args, **kwargs):
        query_params = request.query_params

        page_no = query_params.get('page', 1)
        page_size = query_params.get("page_size", 10)

        coupon_manager = CouponImpl(page=page_no, page_size=page_size)
        response = coupon_manager.search_coupon(query)

        return JsonResponse(response, status=status_codes.HTTP_200_OK)
