from django.contrib import admin
from .models import Cohort, CohortRegistration, Payment

@admin.register(Cohort)
class CohortAdmin(admin.ModelAdmin):
    list_display = ('name', 'mentor', 'start_date', 'end_date', 'price')
    search_fields = ('name', 'description', 'mentor__username')
    list_filter = ('start_date', 'end_date', 'price')
    ordering = ('-start_date',)

@admin.register(CohortRegistration)
class CohortRegistrationAdmin(admin.ModelAdmin):
    list_display = ('get_cohort_name', 'user', 'get_mentor_name', 'registered_at', 'payment_status')
    search_fields = ('user__username', 'cohort__name')
    list_filter = ('payment_status', 'registered_at')
    ordering = ('-registered_at',)
    autocomplete_fields = ['cohort', 'user']  # Cohort first, then user

    # Define the order of fields in the admin form
    fields = ['cohort', 'user', 'payment_status']

    def get_cohort_name(self, obj):
        return obj.cohort.name
    get_cohort_name.short_description = 'Cohort'

    def get_mentor_name(self, obj):
        return obj.cohort.mentor.username
    get_mentor_name.short_description = 'Mentor'


