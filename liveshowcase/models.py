from django.db import models

# Create your models here.
class watch(models.Model):
    classname= models.CharField(max_length=30)
    location= models.CharField(max_length=30)

    class Meta:
        db_table='seetable'