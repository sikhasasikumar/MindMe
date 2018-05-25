from django.db import models
from django.urls import reverse


class Reminder(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    date = models.DateTimeField()

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('view-reminder', kwargs={'pk': self.id})
