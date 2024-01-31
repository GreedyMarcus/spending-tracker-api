from rest_framework import serializers

from .models import Spending


class SpendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spending
        fields = "__all__"
