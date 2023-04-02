from django.contrib import admin
from .models import Employee,Movie
from .models import Students

# Register your models here.
admin.site.register(Employee)
admin.site.register(Students)
admin.site.register(Movie)
