from django.db import models
from django.urls import reverse
from PIL import Image, ImageOps

# Create your models here.

class Photocard(models.Model):
	title = models.CharField(max_length=70)
	description = models.CharField(max_length=400)
	photo = models.ImageField(upload_to='lifestyleuploads',default='lifestyleuploads/nikhilcompressed1.jpg')

	def save(self):
		super().save()
		img = Image.open(self.photo.path)
		size = (700,450)
		img = ImageOps.fit(img, size,Image.ANTIALIAS)
		img.save(self.photo.path)






