from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Books(models.Model):
    title = models.CharField(max_length=255)
    descriptions = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title



