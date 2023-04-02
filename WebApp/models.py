from django.db import models


# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=100,null=True)
    age=models.IntegerField(null=True)
    sal=models.FloatField(max_length=20,null=True)


    def __str__(self) :
        return self.name






class Students(models.Model):
    name=models.CharField(max_length=100,null=True)
    age=models.IntegerField()
    marks1=models.FloatField(max_length=20)    


class Movie(models.Model):
    movie_title=models.CharField(max_length=150)
    release_year=models.IntegerField()
    director=models.CharField(max_length=100)
    movie_poster=models.ImageField(upload_to='static/images/', null=True)
    movie_plot=models.TextField()


    def __str__(self):
        return self.movie_title        
    

  
class Students(models.Model):  
    first_name = models.CharField(max_length=200)  
    last_name = models.CharField(max_length=200)  
    address = models.CharField(max_length=200)  
    roll_number = models.IntegerField()  
    mobile = models.CharField(max_length=10)  
  
    def __str__(self):  
        return self.first_name + " " + self.last_name    