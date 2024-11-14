from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Admin, Item, Category, Supplier
from .serializers import AdminSerializer, ItemSerializer, CategorySerializer, SupplierSerializer

class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    @action(detail=False, methods=['get'])
    def stock_summary(self, request):
        total_items = Item.objects.all()
        total_quantity = sum(item.quantity for item in total_items)
        total_value = sum(item.total_value() for item in total_items)
        average_price = total_value / total_quantity if total_quantity > 0 else 0
        return Response({
            'total_quantity': total_quantity,
            'total_value': total_value,
            'average_price': average_price
        })

    @action(detail=False, methods=['get'])
    def low_stock(self, request):
        low_stock_items = Item.objects.filter(quantity__lt=5)
        return Response(ItemSerializer(low_stock_items, many=True).data)

    @action(detail=False, methods=['get'])
    def category_summary(self, request):
        categories = Category.objects.all()
        summary = []
        for category in categories:
            items_in_category = Item.objects.filter(category=category)
            total_quantity = sum(item.quantity for item in items_in_category)
            total_value = sum(item.total_value() for item in items_in_category)
            average_price = total_value / total_quantity if total_quantity > 0 else 0
            summary.append({
                'category_name': category.name,
                'total_quantity': total_quantity,
                'total_value': total_value,
                'average_price': average_price
            })
        return Response(summary)