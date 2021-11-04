from django.db import models
from datetime import datetime, timedelta


class Card(models.Model):
    name = models.CharField(max_length=30)
    date_create = models.DateTimeField(auto_now_add=True)
    date_activate = models.DateTimeField(default=datetime.now() + timedelta(days=365))
    number = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.number} + {self.name}'


card_test = Card(name='test_second', number=439214)
