from rest_framework import serializers
from .models import NewsTable


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsTable
        fields = "__all__"
