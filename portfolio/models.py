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


class Project(models.Model):
	name = models.CharField(max_length=70)
	description = models.CharField(max_length=10000,blank=True)
	githublink = models.URLField(max_length=1000,blank=True)
	videolink = models.URLField(max_length=1000,blank=True)
	image = models.ImageField(upload_to='projectimages',default='projectimages/defaultproject.jpg')
	technologystack = models.CharField(max_length=5000,blank=True)

	def get_absolute_url(self):
		return '/portfolio/projects/'

class Certificate(models.Model):
	title = models.CharField(max_length=70)
	gdrivelink = models.URLField(max_length=10000)

