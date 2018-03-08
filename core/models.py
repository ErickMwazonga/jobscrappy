# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ScrapedJob(models.Model):
    job_title = models.CharField(max_length=255)
    job_location = models.CharField(max_length=255)
    job_type = models.CharField(max_length=255)
    job_salary = models.CharField(max_length=255)
    time_posted = models.CharField(max_length=255)
    job_category = models.CharField(max_length=255)
    job_link = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.job_title)
