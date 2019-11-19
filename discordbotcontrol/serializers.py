from django.contrib.auth.models import User
from discordbotcontrol.models import Category, Track
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    '''subcategories = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name')
    '''

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.data = validated_data.get('data', instance.data)
        instance.father = validated_data.get('father', instance.father)
        instance.save()
        return instance

    class Meta:
        model = Category
        fields = ['id', 'created_at', 'name',
                  'description', 'subcategorias']
