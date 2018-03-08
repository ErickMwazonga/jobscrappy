# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import ScrapedJob

# Register your models here.
@admin.register(ScrapedJob)
class ScrapedJobAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'job_location', 'job_type', 'job_salary', 'time_posted', 'job_category', 'job_link', 'created_at', 'updated_at')
    search_fields = ('job_title', 'job_location', 'job_type', 'job_salary', 'time_posted', 'job_category', 'job_link', 'created_at', 'updated_at')
    list_filter = ('created_at',)
    ordering = ('-updated_at',)
