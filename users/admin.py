from django.contrib import admin
from .models import User, UserProfile, Education, Experience

# Register your models here.


admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Education)
admin.site.register(Experience)