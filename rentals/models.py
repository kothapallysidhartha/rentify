from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    is_seller = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Property(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.CharField(max_length=100)
    area = models.FloatField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    hospitals_nearby = models.BooleanField(default=False)
    colleges_nearby = models.BooleanField(default=False)

    def __str__(self):
        return self.place
