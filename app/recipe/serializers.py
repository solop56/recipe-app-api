"""
Serializers for recipe
"""
from rest_framework import serializers

from core.models import Recipe

class RecipeSerializers(serializers.ModelSerializer):
    """Serializer for recipe"""

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'time_minutes', 'price', 'link']
        read_only_fields = ['id']

class RecipeDetailsSerializer(RecipeSerializers):
    """Serializer for recipe details view"""

    class Meta(RecipeSerializers.Meta):
        fields = RecipeSerializers.Meta.fields + ['description']