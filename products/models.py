from django.db import models

# Create your models here.


class Collection(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Tags(models.Model):
    """
    A model for the individual flavours of a Product, which can belong to many different
    products.
    """
    class Meta:
        ordering = ['name']

    name = models.CharField(max_length=50, unique=True)
    friendly_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    collection = models.ForeignKey('Collection', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    card_name = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    tags = models.ManyToManyField(Tags)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_description(self):
        return self.description

    def get_tags(self):
        return [self.tags]


class Membership(Product):
    # user = models.ForeignKey('User', on_delete=models.CASCADE)
    is_membership = models.BooleanField(default=True)

    def __str__(self):
        return self.name
