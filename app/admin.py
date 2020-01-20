# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from app.models import Session
from advanced_filters.admin import AdminAdvancedFiltersMixin


class ProfileAdmin(AdminAdvancedFiltersMixin, admin.ModelAdmin):
    def start_time_format(self, obj):
        return obj.start_time.strftime("%H:%M %p")

    def end_time_format(self, obj):
        return obj.end_time.strftime("%H:%M %p")

    def date_format(self, obj):
        return obj.date.strftime("%a %b %d")

    list_display = ['client_name', 'date_format', 'start_time_format', 'duration', 'end_time_format', 'type', 'notes',
                    'status', 'is_accepted']
    # specify which fields can be selected in the advanced filter
    # creation form
    advanced_filter_fields = (
        'client_name',
        'client_name'
    )

    list_filter = ['status', 'is_accepted', 'client_name']


admin.site.register(Session, ProfileAdmin)
