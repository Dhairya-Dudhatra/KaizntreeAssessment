from django.contrib.auth.models import Group, User
from rest_framework import serializers

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['sku', 'name', 'tags', 'category', 'stock_status', 'available_stock']

