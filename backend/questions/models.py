from django.db import models


class Question(models.Model):

    CATEGORY_CHOICES = [
        ('technical', 'Technical'),
        ('hr', 'HR'),
        ('behavioral', 'Behavioral'),
        ('aptitude', 'Aptitude'),
    ]

    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]

    question_text = models.TextField()

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )

    skill = models.CharField(
        max_length=100,
        blank=True
    )

    difficulty = models.CharField(
        max_length=10,
        choices=DIFFICULTY_CHOICES
    )

    expected_answer = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.question_text[:80]