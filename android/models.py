from django.db import models


class Talk(models.Model):
    talk = models.TextField()

    def __str__(self):
        return self.talk
# Create your models here.
