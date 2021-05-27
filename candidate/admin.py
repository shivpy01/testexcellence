from django.contrib import admin

# Register your models here.
from .models import candidate,test_score

admin.site.register(candidate)
admin.site.register(test_score)