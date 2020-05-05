from django.db import models


class City(models.Model):
    name = models.CharField(max_length=20)
    city_id = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'cities'
