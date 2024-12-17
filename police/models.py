from django.db import models

# Create your models here.
class Incident(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('resolved', 'Resolved'),
        ('in_progress', 'In Progress'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    date_reported = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return self.title
