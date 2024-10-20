from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Cloth(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name", default='')
    brand = models.CharField(max_length=255, verbose_name="Brand", default='')
    type_of_clothing = models.CharField(max_length=255, verbose_name="Type of clothing", default='')
    content = models.TextField(blank=True, verbose_name="Description", default='')
    photo = models.ImageField(upload_to="media/Clothes/", verbose_name="Photo1", default='')
    photo2 = models.ImageField(upload_to="media/Clothes/", verbose_name="Photo2", default='', blank=True)
    photo3 = models.ImageField(upload_to="media/Clothes/", verbose_name="Photo3", default='', blank=True)
    rating = models.FloatField(max_length=2, null=0, verbose_name="Rating", default='')
    count_of_votes = models.IntegerField(default=1)
    cost = models.DecimalField(max_digits=10, null=0, decimal_places=0, verbose_name="Cost of Clothing", default='')
    limited = models.BooleanField(default=False, verbose_name="Limited edition?")
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})
    class Meta:
        ordering = ['brand']

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cloth = models.ForeignKey(Cloth, on_delete=models.CASCADE)
    old_rating = models.IntegerField(default='0')
    def __str__(self):
        return self.name
    
class Brand(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    photo = models.ImageField(upload_to="media/Brands/", verbose_name="Photo")
    n_of_subscribers = models.DecimalField(max_digits=100, decimal_places=1, verbose_name="Number of subscribers(VK)")
    rating = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Seller rating")
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    