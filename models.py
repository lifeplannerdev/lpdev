class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    bio = models.TextField()
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.name 