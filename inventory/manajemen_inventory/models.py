from django.db import models

class Admin(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.username

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    admin = models.ForeignKey(Admin, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    def total_value(self):
        return self.quantity * self.price