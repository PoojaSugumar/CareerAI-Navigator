from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skills = models.TextField()  # Store skills as a comma-separated string
    interests = models.TextField()
    experience_level = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class CareerSuggestion(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    user_skills = models.TextField()  # Store skills as comma-separated values
    career_recommendation = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name

    class Meta:
        ordering = ['-created_at']
