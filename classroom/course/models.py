from django.db import models

# Create your models here.
class Course(models.Model):
    id = models.TextField(max_length=100, primary_key=True)
    name = models.TextField(max_length=100)
    des = models.TextField(max_length=100)

    def __str__(self):
        return f'{self.id} {self.name} {self.des}'