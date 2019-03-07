from django.db import models

class Card(models.Model):
    to = models.CharField(max_length=14)
    From = models.CharField(max_length=14)
    title = models.CharField(max_length=50)
    content = models.TextField()
    img = models.ImageField(upload_to="images/")
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title
