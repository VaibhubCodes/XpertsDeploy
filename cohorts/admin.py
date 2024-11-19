from django.contrib import admin
from .models import Cohort, CohortRegistration, Payment

class CohortBaseAdmin(admin.ModelAdmin):
    """Base Admin class to define shared logic."""
    
    def get_cohort_name(self, obj):
        """Returns the name of the cohort."""
        return obj.cohort.name if hasattr(obj, 'cohort') else obj.cohort_registration.cohort.name
    get_cohort_name.short_description = 'Cohort'


@admin.register(Cohort)
class CohortAdmin(admin.ModelAdmin):
    list_display = ('name', 'mentor', 'start_date', 'end_date', 'price')
    search_fields = ('name', 'description', 'mentor__username')
    list_filter = ('start_date', 'end_date', 'price')
    ordering = ('-start_date',)


@admin.register(CohortRegistration)
class CohortRegistrationAdmin(CohortBaseAdmin):
    list_display = ('get_cohort_name', 'user', 'get_mentor_name', 'registered_at', 'payment_status')
    search_fields = ('user__username', 'cohort__name')
    list_filter = ('payment_status', 'registered_at')
    ordering = ('-registered_at',)
    autocomplete_fields = ['cohort', 'user']
    fields = ['cohort', 'user', 'payment_status']

    def get_mentor_name(self, obj):
        """Returns the mentor's username."""
        return obj.cohort.mentor.username
    get_mentor_name.short_description = 'Mentor'


@admin.register(Payment)
class PaymentAdmin(CohortBaseAdmin):
    list_display = ('get_cohort_name', 'user', 'amount', 'payment_status', 'payment_date', 
                    'razorpay_order_id', 'razorpay_payment_id', 'verified')
    search_fields = ('user__username', 'cohort_registration__cohort__name', 
                     'razorpay_order_id', 'razorpay_signature')
    list_filter = ('payment_status', 'payment_date', 'verified')
    ordering = ('-payment_date',)
    autocomplete_fields = ['cohort_registration', 'user']
    fields = ['cohort_registration', 'user', 'amount', 'razorpay_order_id', 
              'razorpay_payment_id', 'payment_status', 'verified']
