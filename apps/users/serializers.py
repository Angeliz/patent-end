from django.contrib.auth import get_user_model
from rest_framework import serializers

# from users.models import Users
Users = get_user_model()

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('username', 'id', 'user_type', 'user_email', 'user_phone_number', 'user_address', 'user_info')


class UsersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('username', 'id', 'user_type', 'user_email', 'user_phone_number', 'user_address', 'user_info')

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'username': instance.username,
            'user_type': instance.user_type,
            'user_email': instance.user_email,
            'user_phone_number': instance.user_phone_number,
            'user_address': instance.user_address,
            'user_info': instance.user_info
        }


class UsersRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('username', 'id', 'user_type', 'user_email', 'user_phone_number', 'user_address', 'user_info')

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'username': instance.username,
            'user_type': instance.user_type,
            'user_email': instance.user_email,
            'user_phone_number': instance.user_phone_number,
            'user_address': instance.user_address,
            'user_info': instance.user_info
        }


class UsersUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('username', 'password', 'user_email', 'user_phone_number', 'user_address', 'user_info')

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.user_info = validated_data.get('user_info', instance.user_info)
        instance.user_email = validated_data.get('user_email', instance.user_email)
        instance.user_phone_number = validated_data.get('user_phone_number', instance.user_phone_number)
        instance.user_address = validated_data.get('user_address', instance.user_address)
        instance.save()
        return instance


class UsersCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('username', 'password', 'user_type')

    def create(self, validated_data):
        user = super(UsersCreateSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        # user.type = validated_data['type']
        user.save()
        return user

    def to_representation(self, instance):
        return {
            'username': instance.username,
            'id': instance.id
        }
