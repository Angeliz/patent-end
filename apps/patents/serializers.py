from rest_framework import serializers

from patents.models import Patents


class PatentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patents
        fields = ('patents_id',
                  'patents_name',
                  'patents_publication_number',
                  'patents_publication_date',
                  'patents_applicant',
                  'patents_inventor',
                  'patents_ipc',
                  'patents_abstract',
                  'patents_area',
                  'patents_field',
                  'patents_score')


class PatentsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patents
        fields = ('patents_id',
                  'patents_name',
                  'patents_publication_number',
                  'patents_publication_date',
                  'patents_applicant',
                  'patents_inventor',
                  'patents_ipc',
                  'patents_abstract',
                  'patents_area',
                  'patents_field',
                  'patents_score')


class PatentsRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patents
        fields = ('patents_id',
                  'patents_name',
                  'patents_publication_number',
                  'patents_publication_date',
                  'patents_applicant',
                  'patents_inventor',
                  'patents_ipc',
                  'patents_abstract',
                  'patents_area',
                  'patents_field',
                  'patents_score')


class PatentsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patents
        fields = ('patents_name',
                  'patents_publication_number',
                  'patents_publication_date',
                  'patents_applicant',
                  'patents_inventor',
                  'patents_ipc',
                  'patents_abstract',
                  'patents_area',
                  'patents_field',
                  'patents_score')

    def update(self, instance, validated_data):
        instance.patents_name = validated_data.get('patents_name', instance.patents_name)
        instance.patents_publication_number = validated_data.get('patents_publication_number', instance.patents_publication_number)
        instance.patents_publication_date = validated_data.get('patents_publication_date', instance.patents_publication_date)
        instance.patents_applicant = validated_data.get('patents_applicant', instance.patents_applicant)
        instance.patents_inventor = validated_data.get('patents_inventor', instance.patents_inventor)
        instance.patents_ipc = validated_data.get('patents_ipc', instance.patents_ipc)
        instance.patents_abstract = validated_data.get('patents_abstract', instance.patents_abstract)
        instance.patents_area = validated_data.get('patents_area', instance.patents_area)
        instance.patents_field = validated_data.get('patents_field', instance.patents_field)
        # instance.patents_in_project = validated_data.get('patents_in_project', instance.patents_in_project)
        instance.patents_score = validated_data.get('patents_score', instance.patents_score)
        instance.save()
        return instance


class PatentsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patents
        fields = ('patents_name',
                  'patents_publication_number',
                  'patents_publication_date',
                  'patents_applicant',
                  'patents_inventor',
                  'patents_ipc',
                  'patents_abstract',
                  'patents_area',
                  'patents_field',
                  'patents_score')

    def create(self, validated_data):
        return Patents.objects.create(**validated_data)

