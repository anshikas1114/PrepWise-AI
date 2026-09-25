from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    EXPERIENCE_LEVELS = [
        ('fresher', 'Fresher'),
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('experienced', 'Experienced'),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )

    full_name = models.CharField(max_length=100)

    education = models.CharField(
        max_length=200,
        blank=True
    )

    skills = models.TextField(blank=True)

    experience_level = models.CharField(
        max_length=20,
        choices=EXPERIENCE_LEVELS,
        default='fresher'
    )

    target_role = models.CharField(
        max_length=100,
        blank=True
    )

    bio = models.TextField(blank=True)

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.full_name