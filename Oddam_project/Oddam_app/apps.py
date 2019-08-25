from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig

class OddamAppConfig(AppConfig):
    name = 'Oddam_app'

class MyAdminConfig(AdminConfig):
    default_site = 'Oddam_project.admin.MyAdminSite'