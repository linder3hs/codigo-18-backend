from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    stock = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    category = models.CharField(max_length=255, null=True, blank=True)
    image = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'products'
