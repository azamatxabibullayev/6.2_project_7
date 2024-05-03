from django.db import models


# Create your models here.

class OfflineComputerGames(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.IntegerField()

    class Meta:
        db_table = 'OfflineComputerGame'

    def __str__(self):
        return self.name


class OnlineComputerGames(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.IntegerField()

    class Meta:
        db_table = 'OnlineComputerGame'

    def __str__(self):
        return self.name
