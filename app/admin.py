from django.contrib import admin
from app.models import *

# Register your models here.




# we are registering our models into admin.py file inorder to store the tables in our models

admin.site.register(Address)
admin.site.register(WorkExperience)
admin.site.register(Qualifications)
admin.site.register(Project)
admin.site.register(Employee)




