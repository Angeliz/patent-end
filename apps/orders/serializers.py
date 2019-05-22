from rest_framework import serializers

from orders.models import Orders


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ('orders_id',
                  'orders_name',
                  'orders_state',
                  'orders_method',
                  'orders_obj',
                  'orders_user',
                  'orders_create_at',
                  'orders_update_at')


class OrdersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ('orders_id',
                  'orders_name',
                  'orders_state',
                  'orders_method',
                  'orders_obj',
                  'orders_user',
                  'orders_create_at',
                  'orders_update_at')


class OrdersRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ('orders_id',
                  'orders_name',
                  'orders_state',
                  'orders_method',
                  'orders_obj',
                  'orders_user',
                  'orders_create_at',
                  'orders_update_at')


class OrdersUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ( 'orders_state', )

    def update(self, instance, validated_data):
        instance.orders_state = validated_data.get('orders_state', instance.orders_state)
        instance.save()
        return instance


class OrdersCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ('orders_name',
                  'orders_state',
                  'orders_method',
                  'orders_obj',
                  'orders_user')

    def create(self, validated_data):
        return Orders.objects.create(**validated_data)

