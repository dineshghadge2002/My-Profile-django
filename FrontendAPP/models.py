from django.db import models

# Create your models here.

class AdditionRecord(models.Model):
    num1 = models.IntegerField()
    num2 = models.IntegerField()
    result = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return f"{self.num1} + {self.num2} = {self.result}"
