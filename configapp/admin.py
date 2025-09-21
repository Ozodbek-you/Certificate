from django.contrib import admin

from configapp.models import *

admin.site.register([User,Teacher,Student])
