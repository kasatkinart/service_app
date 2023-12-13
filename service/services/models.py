from django.core.validators import MaxValueValidator
from django.db import models

from clients.models import Client


# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=50)
    full_price = models.PositiveIntegerField()

    def __str__(self):
        return f'Продукт "{self.name}" с ежемесячной ценой {self.full_price}'


class Plan(models.Model):
    PLAN_TYPES = (
        ('full', 'Full'),
        ('student', 'Student'),
        ('dicsount', 'Discount')
    )

    plan_type = models.CharField(choices=PLAN_TYPES, max_length=10)
    discount_percent = models.PositiveIntegerField(default=0, validators=[MaxValueValidator])

    def __str__(self):
        return f'Тарифный план {self.plan_type} со скидкой {self.discount_percent}%'


class Subscription(models.Model):
    client = models.ForeignKey(Client, related_name='subscriptions', on_delete=models.PROTECT)
    service = models.ForeignKey(Service, related_name='subscriptions', on_delete=models.PROTECT)
    plan = models.ForeignKey(Plan, related_name='subscriptions', on_delete=models.PROTECT)

    def __str__(self):
        return f'Подписка {self.client} на "{self.service}" c {self.plan}'
