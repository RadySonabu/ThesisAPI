from django.contrib import admin
from .models import MyUser, Role


admin.site.register(MyUser)
admin.site.register(Role)