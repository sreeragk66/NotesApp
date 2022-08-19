from django.db import models

# Create your models here.


class Note(models.Model):
    title=models.CharField(max_length=150)
    content=models.TextField()
    created_date=models.DateTimeField(auto_now_add=True,null=True)
    image=models.ImageField(upload_to="noteimages",null=True)



