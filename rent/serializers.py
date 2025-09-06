from rest_framework import serializers
from .models import Rents

class RentSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Rents
        fields = ['id', 'car', 'client', 'rent_date', 'return_date', 'rent_notes', 'total_price']
        depth = 1

    def get_total_price(self, obj):
        days = (obj.return_date - obj.rent_date).days
        if days < 1:
            days = 1

        daily_price = obj.car.individual_price or obj.car.category.category_price
        return daily_price * days
