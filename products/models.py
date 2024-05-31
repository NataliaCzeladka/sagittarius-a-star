from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    PAPERBACK = 'Paperback'
    HARDCOVER = 'Hardcover'

    COVER_TYPE_CHOICES = [
        (PAPERBACK, 'Paperback'),
        (HARDCOVER, 'Hardcover'),
    ]

    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    title = models.CharField(max_length=254)
    author = models.CharField(max_length=254)
    description = models.TextField()
    year = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
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
