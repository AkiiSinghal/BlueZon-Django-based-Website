from django.contrib import admin
from game.models import Match, UserProfileInfo, FreePayUser
# Register your models here.
class MatchAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'available', 'time', 'date', 'prize', 'kills', 'fees', 'type', 'version', 'map', 'entry', 'pay', 'users']
    list_filter = ['available', 'map', 'type', 'fees']
    list_editable = ['name', 'slug', 'available', 'time', 'date', 'prize', 'kills', 'fees', 'type', 'version', 'map', 'entry', 'pay', 'users']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Match, MatchAdmin)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user', 'user_email', 'phone', 'match_played', 'total_kills', 'amount_won']
    list_editable = ['match_played', 'total_kills', 'amount_won']
    search_fields = ['phone', 'user__username']
    def user_email(self, instance):
    	return instance.user.email
admin.site.register(UserProfileInfo, UserAdmin)
class PayUser(admin.ModelAdmin):
    list_display = ['id', 'matchid', 'users']
    list_filter = ['matchid']
admin.site.register(FreePayUser, PayUser)