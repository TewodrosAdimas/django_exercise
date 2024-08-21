from django.contrib import admin
from .import models
# import django.apps
# Register your models here.
# class BlogAdminArea(admin.AdminSite):
#     site_header = "Blog admin area"

# blog_site = BlogAdminArea(name='BlogAdmin')

# blog_site.register(models.Post)
# admin.site.register(models.Post)
#to collect all the models  
# models = django.apps.apps.get_models()
# print(models)

# for model in models:
#     try:
#         admin.site.register(model)

#     except admin.sites.AlreadyRegistered:
#         pass

class BlogAdminArea(admin.AdminSite):
    site_header = "Blog Admin Area"

blog_site = BlogAdminArea(name="BlogAdmin")