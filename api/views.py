from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status

from .models import Spending
from .serializers import SpendingSerializer


class SpendingList(ListCreateAPIView):
    serializer_class = SpendingSerializer

    def get_queryset(self):
        queryset = Spending.objects.all()

        currency = self.request.query_params.get("currency")
        order = self.request.query_params.get("order")

        if currency and currency not in ["HUF", "USD"]:
            return Response(
                {"error": "Currency must be on of the following values: 'HUF' or 'USD'."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if order and order not in ["spent_at", "-spent_at", "amount", "-amount"]:
            return Response(
                {"error": "Order must be on of the following values: 'spent_at', '-spent_at', 'amount' or '-amount'."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if currency is not None:
            queryset = queryset.filter(currency=currency)

        if order is not None:
            queryset = queryset.order_by(order)

        return queryset
