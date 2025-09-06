from rest_framework import serializers
from .models import Rents

class RentSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Rents
        fields = ['id', 'car', 'client', 'rent_date', 'return_date', 'rent_notes', 'total_price']

    def get_total_price(self, obj):
        # Вычисляем количество дней
        days = (obj.return_date - obj.rent_date).days
        if days < 1:
            days = 1  # минимальный 1 день аренды

        # Если цена машины = 0, берём цену категории
        if obj.car.individual_price == 0:
            daily_price = obj.car.category.category_price
        else:
            daily_price = obj.car.individual_price

        return daily_price * days

    def create(self, validated_data):
        return Rents.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.car = validated_data.get('car', instance.car)
        instance.client = validated_data.get('client', instance.client)
        instance.rent_date = validated_data.get('rent_date', instance.rent_date)
        instance.return_date = validated_data.get('return_date', instance.return_date)
        instance.rent_notes = validated_data.get('rent_notes', instance.rent_notes)
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()
        return instance
    
    def partial_update(self, instance, validated_data):
        return self.update(instance, validated_data)
    
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'car': instance.car,
            'client': instance.client,
            'rent_date': instance.rent_date,
            'return_date': instance.return_date,
            'rent_notes': instance.rent_notes,
            'total_price': instance.total_price,
        }
    
    def to_internal_value(self, data):
        return {
            'car': data.get('car'),
            'client': data.get('client'),
            'rent_date': data.get('rent_date'),
            'return_date': data.get('return_date'),
            'rent_notes': data.get('rent_notes'),
        }
    
    