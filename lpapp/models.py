
from django.db import models

class Appointment(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    message=models.TextField(max_length=500,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
          return self.firstname


class Webinar(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
          return self.name
    
class Team(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    img = models.ImageField(upload_to='gallery')
    bio = models.TextField(max_length=500)
    post = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Review(models.Model):
    team_member = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="reviews")
    name = models.CharField(max_length=100)
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.name} for {self.team_member.name}"
    
class Immigration(models.Model):
    candidate = models.CharField(max_length=250)
    phno = models.BigIntegerField()  # Use BigIntegerField for larger phone numbers
    field = models.CharField(max_length=250)
    exp = models.IntegerField()

    def __str__(self):
        return self.candidate
