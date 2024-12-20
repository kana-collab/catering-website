from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import (
    websiteDetail,HomeSection, AboutSection, WhyChooseSection, MenuCategory, 
    MenuItem, EventsSection, BookADateSection, BookADateForm, ContactSection
)

admin.site.register(websiteDetail)
admin.site.register(HomeSection)
admin.site.register(AboutSection)
admin.site.register(WhyChooseSection)
admin.site.register(MenuCategory)
admin.site.register(MenuItem)
admin.site.register(EventsSection)
admin.site.register(BookADateSection)
admin.site.register(BookADateForm)
admin.site.register(ContactSection)
