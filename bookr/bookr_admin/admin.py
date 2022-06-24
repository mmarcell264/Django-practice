from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path


# Register your models here.
class BookrAdmin(admin.AdminSite):
    site_header = "Bookr Administration Portal"
    site_title = "Bookr Aministration Portal"
    index_title = "Bookr Administration"
    logout_template = 'admin/logout.html'

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('admin_profile/', self.admin_view(self.profile_view)),
        ]
        return my_urls + urls

    def profile_view(self, request):
        request.current_app = self.name
        print(self.name)
        context = self.each_context(request)

        return TemplateResponse(request, "admin/admin_profile.html", context)




