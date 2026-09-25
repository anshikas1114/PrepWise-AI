from django.db import models
from django.contrib.auth.models import User


class Recommendation(models.Model):

    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recommendations'
    )

    topic = models.CharField(max_length=100)

    reason = models.TextField()

    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='medium'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.topic}"