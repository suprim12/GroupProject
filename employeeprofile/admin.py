from django.contrib import admin
from .models import EmployeeProfile,Experience,Skill,Degree,Project,Cv
# Register your models here.

admin.site.register(EmployeeProfile)
admin.site.register(Experience)
admin.site.register(Skill)
admin.site.register(Degree)
admin.site.register(Cv)
