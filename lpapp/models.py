from django.utils.text import slugify
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


# class Careers(models.Model):
#     job_title=models.CharField(max_length=255)
#     job_mode=models.CharField(max_length=255)
#     job_salary=models.CharField(max_length=255)
#     job_location=models.CharField(max_length=255)
#     job_type=models.CharField(max_length=255)
#     job_exp=models.CharField(max_length=255)
#     job_details = models.TextField()
#     slug = models.SlugField(max_length=255, unique=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.job_title

from django.utils.text import slugify

class Careers(models.Model):
    JOB_MODE_CHOICES = [
        ('remote', 'Remote'),
        ('onsite', 'Onsite'),
        ('hybrid', 'Hybrid'),
    ]

    JOB_TYPE_CHOICES = [
        ('internship', 'Internship'),
        ('full_time', 'Full-time'),
        ('contract', 'Contract'),
    ]

    job_title = models.CharField(max_length=255, verbose_name="Job Title")
    job_mode = models.CharField(max_length=50, choices=JOB_MODE_CHOICES, verbose_name="Job Mode")
    job_salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Salary")
    job_location = models.CharField(max_length=255, verbose_name="Location")
    job_type = models.CharField(max_length=50, choices=JOB_TYPE_CHOICES, verbose_name="Job Type")
    job_exp = models.CharField(max_length=255, verbose_name="Experience Level", blank=True, null=True)
    job_details = models.TextField(verbose_name="Job Details")
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    def __str__(self):
        return self.job_title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.job_title)
        super().save(*args, **kwargs)


    