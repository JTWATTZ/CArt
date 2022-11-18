from django.db import models

class Produce(models.Model):
    title = models.CharField(max_length = 200)
    fruit = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
# below str method prints out name of instance in db
    def __str__(self):
        return self.title

class Cart(models.Model):
    total = models.DecimalField(max_digits=5, decimal_places=2)
    produce = models.ForeignKey( Produce, on_delete=models.CASCADE)  



