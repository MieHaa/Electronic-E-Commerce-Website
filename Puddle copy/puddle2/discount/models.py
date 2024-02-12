from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Discount(models.Model):
    code = models.CharField(max_length=20)
    percent = models.IntegerField(
        validators=[
            MinValueValidator(0, message="Value must be greater than or equal to 0."),
            MaxValueValidator(100, message="Value must be less than or equal to 100."),
        ]
    )

    class Meta:
        ordering = ('code',)
        verbose_name_plural = 'Discounts'

    def __str__(self):
        return self.code
