from django.contrib import admin
from .models import Specialization, Designation, AvailableTime, Doctor, Review
# Register your models here.

class SpceializationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class DesignationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Specialization, SpceializationAdmin)
admin.site.register(Designation, DesignationAdmin)
admin.site.register(AvailableTime)
admin.site.register(Doctor)
admin.site.register(Review)