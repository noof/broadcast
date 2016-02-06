from django.contrib import admin
from .models import Group, TwitterKeys
#from .models import GroupMeAPI

#admin.site.register(GroupMeGroup)
class GroupAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['group_name', 'group_id', 'active']})
	]
	#inlines = [GroupInline]
	list_display = ['group_name']

admin.site.register(Group, GroupAdmin)