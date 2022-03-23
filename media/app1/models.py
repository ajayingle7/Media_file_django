from django.db import models

# Create your models here.


class Naukari(models.Model):
    eid = models.IntegerField()
    ename = models.CharField(max_length=50)
    resume = models.FileField(upload_to="media")


    def __str__(self):
        return f"{self.eid}--{self.ename}--{self.resume}"


