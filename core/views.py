# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from bs4 import BeautifulSoup
import requests

from django.views.generic import ListView, TemplateView
from django.shortcuts import render

from .models import ScrapedJob

# Create your views here.
def scrape():
    jobs = []

    for page in range(0, 1):
        page = page + 1
        url = "https://www.brightermonday.co.ke/jobs?page={}".format(str(page))


        # Request URL and Beautiful Parser
        source = requests.get(url)
        soup = BeautifulSoup(source.text, "lxml")

        all_articles = soup.find_all('article')

        for article in all_articles:
            data = {}

            for job in article.find_all('header', class_='search-result__header'):

                # job-title
                job_title = job.find('a', class_='search-result__job-title').text
                data['job-title'] = job_title

                # job-link
                job_link = job.find('div', class_='flex--4').a.get('href')
                data['job-link'] = job_link

                # job-location
                job_location = job.find('div', class_='search-result__location').a.text
                data['job-location'] = job_location

                # job-type
                job_type = job.find('div', class_='search-result__job-type').text.replace('\n', '')
                data['job-type'] = job_type

                # job-salary
                job_salary = job.find('div', class_='search-result__job-salary').text.replace('\n', '')
                data['job-salary'] = job_salary

                # time-posted
                job_time_posted = job.find('div', class_='search-result__job-meta').text.replace('\n', '').split('by')[0]
                data['job-time-posted'] = job_time_posted

                # company-name
                job_company_name = job.find('div', class_='search-result__job-meta').a.text.replace('\n', '')
                data['job-company-name'] = job_company_name

                # company-name-href
                # job-category
                job_category = job.find('div', class_='search-result__job-category').a.text
                data['job-category'] = job_category

                # add to the db table
                # scraped_job = ScrapedJob.objects.get_or_create()(
                ScrapedJob.objects.get_or_create(
                    job_title=job_title,
                    job_location=job_location,
                    job_type=job_type,
                    job_salary=job_salary,
                    time_posted=job_time_posted,
                    job_category=job_category,
                    job_link=job_link
                )
                # scraped_job.save()

                jobs.append(data)

    return jobs

    # return JsonResponse({'jobs': jobs })

# index view
class IndexView(TemplateView):
    template_name = 'core/index.html'

class ScrapeListView(ListView):
    model = ScrapedJob
    context_object_name = 'jobs'
    template_name = 'core/scrape_list.html'
    paginate_by = 10

    def __init__(self, **kwargs):
        scrape()
        return super(ScrapeListView, self).__init__(**kwargs)

    def get_queryset(self):
        return super(ScrapeListView, self).get_queryset().order_by('-created_at')


def api(request):
    return JsonResponse({'jobs': scrape() })
