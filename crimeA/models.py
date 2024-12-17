from django.conf import settings
from django.db import models

# Crime Report model
class CrimeReport(models.Model):
    CATEGORY_CHOICES = [
        ('theft', 'Theft'),
        ('assault', 'Assault'),
        ('vandalism', 'Vandalism'),
        ('other', 'Other'),
    ]
    reporter = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Reference AUTH_USER_MODEL instead of directly using User
        on_delete=models.CASCADE,
        related_name='reported_crimes'  # Optional: For reverse relationship naming
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    location = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)  # Latitude
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)  # Longitude
    evidence_image = models.ImageField(upload_to='evidence_photos/', blank=True, null=True)  # For uploading evidence
    date_reported = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.category}"

# Example for a Notification model (if you have one):
class Notification(models.Model):
    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Reference AUTH_USER_MODEL
        on_delete=models.CASCADE,
        related_name='notifications'  # Optional: For reverse relationship naming
    )
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification to {self.recipient.username}"
