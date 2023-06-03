from django.db import models

# Create your models here.
from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image=models.ImageField(null=True)

    def __str__(self):
        return self.name



class Project(models.Model):
    title = models.CharField(max_length=255,null=True)
    description = models.TextField(max_length=255,null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2,default=True,null=True)
    image = models.ImageField(upload_to="images", height_field=None,default=True,null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title




class register(models.Model):

    username=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    password=models.CharField(max_length=255)
    # place=models.TextField(max_length=255)

class Contribution(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    contributor_name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    user=models.ForeignKey(register,on_delete=models.CASCADE,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        f=f"{self.contributor_name} contributed {self.amount} to project {self.project.title}"
        return f



# Create your models here.
