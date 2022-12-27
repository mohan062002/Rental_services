from django.contrib import admin
from user.models import Owner,User,rooms

class OwnerAdmin(admin.ModelAdmin):
    list_display=(
        'owner_name',
    'owner_username',
    'owner_email',
    'owner_mobile',
    'owner_passward',
    'owner_confirmpass',
    )

admin.site.register(Owner,OwnerAdmin)

class roomsAdmin(admin.ModelAdmin):
    list_display=(
         'p_type',
    'p_name',
    'p_adress',
    'p_city',
    'p_email',
    'vacancy',
    'p_monthly',
    'p_facilities',
    'p_img',
    )
admin.site.register(rooms,roomsAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display=(

        'user_name',
    'user_username',
    'user_email',
    'user_city',
    'user_passward',
    
    'user_confirmpass',
    )

admin.site.register(User,UserAdmin)
# Register your models here.


