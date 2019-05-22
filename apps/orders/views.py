from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from orders.models import Orders
from orders.serializers import OrdersCreateSerializer, OrdersUpdateSerializer, OrdersRetrieveSerializer, OrdersSerializer, OrdersListSerializer


class OrdersViewSet(ModelViewSet):
    queryset = Orders.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return OrdersListSerializer
        elif self.action == 'create':
            return OrdersCreateSerializer
        elif self.action in ('update', 'partial_update'):
            return OrdersUpdateSerializer
        elif self.action == 'retrieve':
            return OrdersRetrieveSerializer
        else:
            return OrdersSerializer

    # @action(detail=False)
    # def get_order(self, request):
    #     """
    #     通过用户id获取订单
    #     """
    #     empty_order = Orders.objects.filter(orders_client=int(request.query_params.get('user'))).order_by('orders_create_at')
    #     serializer = self.get_serializer(empty_order, many=True)
    #     return Response(serializer.data)
