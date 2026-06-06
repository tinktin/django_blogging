from django.contrib import admin
from .models import About,SocialLink

class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count = About.objects.all().count()
        if count == 0:
            return True
        return False
    def change_view(self, request, object_id, extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save_and_add_another'] = False
        return super().change_view(request, object_id, extra_context=extra_context)
    def add_view(self, request, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save_and_add_another'] = False
        return super().add_view(
            request, form_url, extra_context=extra_context
        )
admin.site.register(About,AboutAdmin)
admin.site.register(SocialLink)



