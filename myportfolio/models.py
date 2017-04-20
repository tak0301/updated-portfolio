import datetime

from django.db import models
from django.utils import timezone
from tinymce import models as tinymce_models


class Project(models.Model):
    project_title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    competencies = models.CharField(max_length=200)
    technologies = models.CharField(max_length=200)
    project_description = tinymce_models.HTMLField()
    small_image = models.FileField()
    large_image = models.FileField()

    def __str__(self):
        return self.project_title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Contact(models.Model):
    email = models.CharField(max_length=200),
    message = models.TextField()

    def __str__(self):
        return self.email
