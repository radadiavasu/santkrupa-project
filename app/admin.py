from django.contrib import admin
from app.models import *
# Register your models here.

@admin.register(SliderImage)
class SliderImageAdmin(admin.ModelAdmin):
    pass

class NavigationLinkInline(admin.TabularInline):
    model = NavigationLink
    extra = 1

@admin.register(Header)
class HeaderAdmin(admin.ModelAdmin):
    inlines = [NavigationLinkInline]

@admin.register(NavigationLink)
class NavigationLinkAdmin(admin.ModelAdmin):
    pass

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    pass

@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    pass

@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    pass

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    pass

admin.site.register(GalleryImage)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    pass

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass