from django.db import models

# Create your models here.


class Medicine(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    unit = models.CharField(max_length=30)
    class_name = models.CharField(max_length=255)
    packaging = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class DetailPurchase(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_purchase = models.ForeignKey('Purchase', on_delete=models.CASCADE)
    expired_date = models.BigIntegerField()
    purchase_price = models.FloatField()
    amount_buy = models.IntegerField()
    sub_total_buy = models.DecimalField(max_digits=10, decimal_places=2)
    percent_buying_margin = models.PositiveSmallIntegerField()
    product = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Purchase(models.Model):
    id = models.BigAutoField(primary_key=True)
    no_notes = models.CharField(max_length=15)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    id_distributor = models.ForeignKey('Distributor', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=255)

    role_choice = [
        ('admin', 'admin'),
        ('kasir', 'kasir'),
        ('owner', 'owner'),
        ('pemilik', 'pemilik')
    ]

    role = models.CharField(max_length=50, choices=role_choice)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Sell(models.Model):
    id = models.BigAutoField(primary_key=True)
    no_notes = models.CharField(max_length=15)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class DetailSell(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_sell = models.ForeignKey('Sell', on_delete=models.CASCADE)
    sell_price = models.FloatField()
    amount_sell = models.IntegerField()
    sub_total_sell = models.DecimalField(max_digits=10, decimal_places=2)
    product = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Distributor(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


