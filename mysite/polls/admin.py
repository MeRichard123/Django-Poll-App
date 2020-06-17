from django.contrib import admin

# Register your models here.
# This adds models to the admin site
# for this run python manage.py createsuperuser to make a login to thee site

from .models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)
