from rest_framework import serializers

from projects.models import Projects


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('projects_id', 'projects_name', 'projects_info', 'projects_type', 'projects_area', 'projects_field', 'projects_background', 'projects_feature', 'projects_score')


class ProjectsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('projects_id', 'projects_name', 'projects_info', 'projects_type', 'projects_area', 'projects_field', 'projects_background', 'projects_feature', 'projects_score')


class ProjectsRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('projects_id', 'projects_name', 'projects_info', 'projects_type', 'projects_area', 'projects_field', 'projects_background', 'projects_feature', 'projects_score')


class ProjectsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('projects_name', 'projects_info', 'projects_type', 'projects_area', 'projects_field', 'projects_background', 'projects_feature', 'projects_score')

    def update(self, instance, validated_data):
        instance.projects_name = validated_data.get('projects_name', instance.projects_name)
        instance.projects_info = validated_data.get('projects_info', instance.projects_info)
        instance.projects_type = validated_data.get('projects_type', instance.projects_type)
        instance.projects_area = validated_data.get('projects_area', instance.projects_area)
        instance.projects_field = validated_data.get('projects_field', instance.projects_field)
        instance.projects_background = validated_data.get('projects_background', instance.projects_background)
        instance.projects_feature = validated_data.get('projects_feature', instance.projects_feature)
        instance.projects_score = validated_data.get('projects_score', instance.projects_score)
        instance.save()
        return instance


class ProjectsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('projects_name', 'projects_info', 'projects_type', 'projects_area', 'projects_field', 'projects_background', 'projects_feature', 'projects_score')

    def create(self, validated_data):
        return Projects.objects.create(**validated_data)

