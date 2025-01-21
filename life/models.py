from django.db import models

# Create your models here.


class GameState(models.Model):
    grid = models.JSONField()
    width = models.IntegerField(default=50)
    height = models.IntegerField(default=50)
    created_at = models.DateTimeField(auto_now_add=True)