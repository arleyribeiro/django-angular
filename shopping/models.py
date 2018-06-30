from django.db import models

# Create your models here.
from django.db import models

class ShoppingItem(models.Model):

	name = models.CharField(max_length=60)
	quantity = models.PositiveSmallIntegerField()
	checked = models.BooleanField(default=False)
