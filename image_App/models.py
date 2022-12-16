from django.db import models

# Create your models here.
class emp_details(models.Model):
    emp_name = models.CharField(max_length=100,null=True)
    emp_num = models.IntegerField()
    address = models.CharField(max_length=100,null=True)
    image = models.ImageField(upload_to="image/", null=True)