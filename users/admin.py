from django.contrib import admin
from users.models import Users
# Register your models here.

@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','email','is_staff','date_joined','is_active','last_login')

admin.site.site_header="数据中心后台"
admin.site.site_title="数据中心"
