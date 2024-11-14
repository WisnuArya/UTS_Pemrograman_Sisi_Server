# inventory/urls.py
from django.urls import path, include
from django.http import HttpResponse
from rest_framework.routers import DefaultRouter
from manajemen_inventory.views import AdminViewSet, ItemViewSet, CategoryViewSet, SupplierViewSet

# Router API
router = DefaultRouter()
router.register(r'admins', AdminViewSet)
router.register(r'items', ItemViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'suppliers', SupplierViewSet)

# Fungsi untuk menampilkan halaman utama
def home(request):
    return HttpResponse("Welcome to the Inventory API!")

urlpatterns = [
    path('', home),  # Tambahkan root URL yang mengarah ke home view
    path('api/', include(router.urls)),
]