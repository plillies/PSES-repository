from django.db import models

# Create your database models here.

from django.utils import timezone
from django.utils.text import slugify

class Results(models.Model):
   class Meta:
      verbose_name_plural = "results" # Otherwise Results gets a double s when pluarlized by Django
   title = models.CharField(max_length=250,default='Summary') # Prefix to most names. Usually unchanged.
   code = models.CharField(max_length=50) # Uniquely attributes the file to an entity or demographic group
   # code will appear in the context of an automatcially generated webpage to allow the user to select this file.

   filter = models.CharField(max_length=5,default='0') # Set filter to dpt for automatically generated departmental page
   year = models.CharField(max_length=4,null=True,blank=True) # To satisfy database requirements without recreating database
   language = models.CharField(max_length=2,default='en')
   
   @property # Adds a function to the class Results
   def name(self):
     name = f"{self.title} {self.code} {self.year} {self.language}" # This is the name that appears in the db manager
     return name

   # Override the save() method of the model to automatically generate the slug field
   def save(self, *args, **kwargs): # Defines the save function
     self.slug = slugify(self.code + self.year) # Defines the slug
     super(Results, self).save(*args, **kwargs)

   file = models.FileField(upload_to='data') # data is the default, so saves files to data/data. data can be sandbox.
#   url = models.URLField(null=True,blank=True) # Null and blank satisfy database requirements without recreating database
   created = models.DateTimeField(default=timezone.now)
   updated = models.DateTimeField(auto_now=True)

   def __str__(self): # Returns the name to the db manager
     return self.name

