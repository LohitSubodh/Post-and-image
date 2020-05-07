import uuid
from django.db import models

# Create your models here.
class Post(models.Model):
	title        = models.TextField()

	createdDate = models.DateField()
	uuidNumber         = models.UUIDField()
	images       =models.ImageField(upload_to ='uploads/')
