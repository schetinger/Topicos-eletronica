from django.db import models

class Carta(models.Model):
    media = models.FloatField(default=0)
    dp = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
