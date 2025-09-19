from django.contrib import admin
from .models import Service
from .models import Testimonial



@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'rating', 'approved', 'created_at']
    list_filter = ['approved', 'rating', 'created_at']
    search_fields = ['name', 'location', 'testimonial_text']
    actions = ['approve_testimonials']

    def approve_testimonials(self, request, queryset):
        queryset.update(approved=True)
    approve_testimonials.short_description = "Aprobar testimonios seleccionados"



@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'short_description']
