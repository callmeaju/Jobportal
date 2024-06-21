from django.contrib import admin
from Myapp.models import  Job,Category
# Register your mode
admin.site.register(Category)
admin.site.register(Job)