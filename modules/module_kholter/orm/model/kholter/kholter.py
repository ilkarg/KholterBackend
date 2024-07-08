from django.db import models

class Kholter(models.Model):
    class Meta:
        app_label = 'project'
    start_time = models.TimeField()
    end_time = models.TimeField()
    about = models.TextField()
