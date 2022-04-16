from django.contrib import admin
from .models import Session, SessionData, UserSession

admin.site.register(Session)
admin.site.register(SessionData)
admin.site.register(UserSession)
