from django.db import models
from django.contrib.auth.models import User, AbstractUser


class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    inn = models.CharField('ИНН', max_length=64, db_index=True)
    account = models.DecimalField('счёт', max_digits=11, decimal_places=2)

    def __str__(self):
        return self.user.get_username()
