from django.db import models
from django.contrib.auth.models import User


class Interview(models.Model):

    INTERVIEW_TYPES = [
        ('technical', 'Technical'),
        ('hr', 'HR'),
        ('behavioral', 'Behavioral'),
        ('mixed', 'Mixed'),
    ]

    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='interviews'
    )

    interview_type = models.CharField(
        max_length=20,
        choices=INTERVIEW_TYPES
    )

    target_role = models.CharField(
        max_length=100
    )

    difficulty = models.CharField(
        max_length=10,
        choices=DIFFICULTY_CHOICES
    )

    score = models.FloatField(default=0)

    started_at = models.DateTimeField(
        auto_now_add=True
    )

    completed_at = models.DateTimeField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.interview_type}"


class Response(models.Model):

    interview = models.ForeignKey(
        Interview,
        on_delete=models.CASCADE,
        related_name='responses'
    )

    question = models.ForeignKey(
        'questions.Question',
        on_delete=models.CASCADE,
        related_name='responses'
    )

    answer = models.TextField()

    score = models.FloatField(default=0)

    similarity_score = models.FloatField(default=0)

    feedback = models.TextField(blank=True)

    submitted_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Response - {self.interview.user.username}"