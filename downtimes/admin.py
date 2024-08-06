from django.contrib import admin

from .models import Log, Workorder, ErrorCode

admin.site.register(Log)
admin.site.register(Workorder)
admin.site.register(ErrorCode)
