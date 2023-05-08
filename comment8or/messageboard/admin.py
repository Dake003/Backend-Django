from django.contrib import admin
from django.contrib.admin import AdminSite
# Register your models here.

class ComAdminSite(AdminSite):
    title_header = 'c8 site admin'
    site_header = 'c8admin'
    index_title = 'c8dmin'
    logout_template = 'logged_out.html'

admin_site = ComAdminSite(name='com8nt')
