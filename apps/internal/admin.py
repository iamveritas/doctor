from django.contrib import admin
from apps.internal.models import (Doctor, Region, City,
                                  Hospital, HospitalType, Speciality, Efficiency,
                                  Quality, Respect, Bribery, Comment, Like, Recommendation)


admin.site.register(Doctor)
admin.site.register(Comment)
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
