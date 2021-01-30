from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=40,null=False,blank=False)
    description = models.TextField(null=False)
    members_present = models.ManyToManyField(User,null=True,blank=True,related_name="mem_present")
    members_not_approved = models.ManyToManyField(User,null=True,blank=True,related_name="mem_not_approved")
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    owner = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    def __str__(self):
        return f"{self.name}"

class Comment(models.Model):
    text=  models.TextField(null=False)
    owner = models.ForeignKey(User,blank=False,on_delete=models.CASCADE)
    project = models.ForeignKey(Project,blank=False,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.text} on {self.project}"