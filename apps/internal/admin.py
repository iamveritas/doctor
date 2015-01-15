#-*-coding:utf8-*-
from django.contrib import admin
from apps.internal.models import (Doctor, Region, City,
                                  Hospital, HospitalType, Speciality, Efficiency,
                                  Quality, Respect, Bribery, Comment, Like, Recommendation,
                                  CommentAnswer, )


def make_active(modeladmin, request, queryset):
    queryset.update(is_active=True)
make_active.short_description = "Make active"


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'is_active']
    ordering = ['-created']
    actions = [make_active]


admin.site.register(Doctor)
admin.site.register(Comment, CommentAdmin)
admin.site.register(CommentAnswer)
admin.site.register(Hospital)
admin.site.register(HospitalType)
admin.site.register(City)
admin.site.register(Region)
admin.site.register(Speciality)
#admin.site.register(Efficiency)
#admin.site.register(Quality)
#admin.site.register(Respect)
#admin.site.register(Bribery)
admin.site.register(Like)
admin.site.register(Recommendation)
