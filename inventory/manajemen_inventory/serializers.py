from rest_framework import serializers
from .models import Admin, Item, Category, Supplier

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer()  # Field nested
    supplier = SupplierSerializer()

    class Meta:
        model = Item
        fields = ['name', 'category', 'supplier', 'quantity', 'price']
        
    def create(self, validated_data):
        category_data = validated_data.pop('category')  # Memisahkan data category dari validated_data
        supplier_data = validated_data.pop('supplier')
        supplier = Supplier.objects.create(**supplier_data)
        category = Category.objects.create(**category_data)  # Membuat objek kategori baru
        item = Item.objects.create(supplier=supplier, category=category, **validated_data)
        return item
    
    