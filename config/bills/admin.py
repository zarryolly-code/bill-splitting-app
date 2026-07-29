from django.contrib import admin
from .models import Group, Member, Expense

admin.site.register(Group)
admin.site.register(Member)
admin.site.register(Expense)
