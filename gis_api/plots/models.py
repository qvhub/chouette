from django.contrib.gis.db import models
from django.contrib.auth import get_user_model

class Plot(models.Model):
    name = models.CharField(max_length=255)
    zone = models.PolygonField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    def area_in_hectares(self):

        return round((self.zone.transform(5070, clone=True).area /10000), 2)
 