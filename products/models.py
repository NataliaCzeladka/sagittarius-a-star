from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from decimal import Decimal


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


def current_year():
    return timezone.now().year


class Product(models.Model):
    PAPERBACK = 'Paperback'
    HARDCOVER = 'Hardcover'

    COVER_TYPE_CHOICES = [
        (PAPERBACK, 'Paperback'),
        (HARDCOVER, 'Hardcover'),
    ]

    """Generate choices for years from 1980 to current year"""
    YEAR_CHOICES = [(year, year) for year in range(1960, current_year() + 1)]

    RATING_CHOICES = [
        (Decimal('1.0'), '1.0'),
        (Decimal('1.5'), '1.5'),
        (Decimal('2.0'), '2.0'),
        (Decimal('2.5'), '2.5'),
        (Decimal('3.0'), '3.0'),
        (Decimal('3.1'), '3.1'),
        (Decimal('3.2'), '3.2'),
        (Decimal('3.3'), '3.3'),
        (Decimal('3.4'), '3.4'),
        (Decimal('3.5'), '3.5'),
        (Decimal('3.6'), '3.6'),
        (Decimal('3.7'), '3.7'),
        (Decimal('3.8'), '3.8'),
        (Decimal('3.9'), '3.9'),
        (Decimal('4.0'), '4.0'),
        (Decimal('4.1'), '4.1'),
        (Decimal('4.2'), '4.2'),
        (Decimal('4.3'), '4.3'),
        (Decimal('4.4'), '4.4'),
        (Decimal('4.5'), '4.5'),
        (Decimal('4.6'), '4.6'),
        (Decimal('4.7'), '4.7'),
        (Decimal('4.8'), '4.8'),
        (Decimal('4.9'), '4.9'),
        (Decimal('5.0'), '5.0'),
    ]

    category = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    title = models.CharField(max_length=254)
    author = models.CharField(max_length=254)
    description = models.TextField()
    year = models.IntegerField(
        validators=[
            MinValueValidator(1980), MaxValueValidator(current_year())],
        choices=YEAR_CHOICES,
        default=current_year()
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
    )
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        null=True,
        blank=True,
        validators=[MinValueValidator(1.0), MaxValueValidator(5.0)],
        choices=RATING_CHOICES
    )
    is_new = models.BooleanField(default=False, null=True, blank=True)
    is_bestseller = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    cover_type = models.CharField(
        max_length=10,
        choices=COVER_TYPE_CHOICES,
        default=PAPERBACK,
    )

    def __str__(self):
        return self.title
