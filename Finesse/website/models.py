from django.db import models
from django.utils import timezone


# Create your models here.

class Type(models.Model):
    TYPE = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    type = models.CharField(choices=TYPE, max_length=50)

    def __str__(self):
        return self.type


class Categories(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Filter_Price(models.Model):
    FILTER_PRICE = (
        ('$50 TO $100', '$50 TO $100'),
        ('$101 TO $150', '$101 TO $150'),
        ('$151 TO $200', '$151 TO $200'),
        ('$201 TO $300', '$201 TO $300'),
    )

    price = models.CharField(choices=FILTER_PRICE, max_length=50)

    def __str__(self):
        return self.price



class Filter_Size(models.Model):
    FILTER_SIZE = (
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),

    )

    size = models.CharField(choices=FILTER_SIZE, max_length=50)
    def __str__(self):
        return self.size

class Clothes(models.Model):
    unique_id = models.CharField(unique=True, max_length=200, null=False)
    image = models.ImageField(upload_to='static/Clothes_images/img')
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    filter_price = models.ForeignKey(Filter_Price, on_delete=models.CASCADE)
    size = models.ForeignKey(Filter_Size, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.unique_id is None and self.created_date and self.id:
            self.unique_id = self.created_date.strftime('75%Y%m%d23') + str(self.id)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}, {self.filter_price}'



class Images(models.Model):
    image = models.ImageField(upload_to='Clothes_images/img')
    clothes = models.ForeignKey(Clothes, on_delete=models.CASCADE)