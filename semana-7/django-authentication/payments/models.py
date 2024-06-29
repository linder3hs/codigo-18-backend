from django.db import models
from django.contrib.auth.models import User


class Payment(models.Model):
    payment_id = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.payment_id} - {self.user.first_name}"

    class Meta:
        db_table = 'payments'
