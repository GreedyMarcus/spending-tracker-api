from django.db import models


class Spending(models.Model):
    class Currency(models.TextChoices):
        HUF = "HUF", "HUF"
        USD = "USD", "USD"

    description = models.CharField(max_length=255)
    amount = models.FloatField()
    spent_at = models.DateTimeField()
    currency = models.CharField(max_length=3, choices=Currency.choices)

    def __str__(self):
        return self.description
