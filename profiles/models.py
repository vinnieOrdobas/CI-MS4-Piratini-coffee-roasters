import uuid

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField
from products.models import Product


class UserProfile(models.Model):
    '''
    A user profile model for maintaning default delivery
    information and order history
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=40, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='', null=True, blank=True)

    def __str__(self):
        return self.user.username


class Membership(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=False, blank=False, related_name="membership")
    product = models.ManyToManyField(Product, related_name='membership_product')
    number = models.CharField(max_length=32, null=False, editable=False)

    def __str__(self):
        return f'Membership number {self.number} belonging to {self.user_profile}'

    def generate_membership_number(self):
        """
        Generate a random, unique membership number using UUID
        """
        self.number = uuid.uuid4().hex.upper()
        self.save()


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()
