from django.db import models


# Create your models here.


class OfflineMobileGames(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.IntegerField()

    class Meta:
        db_table = 'OfflineMobileGame'

    def __str__(self):
        return self.name


class OnlineMobileGames(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.IntegerField()

    class Meta:
        db_table = 'OnlineMobileGame'

    def __str__(self):
        return self.name
