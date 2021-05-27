from django.contrib import admin
from .models import TodoItem, DoneTodo

class TodoItemAdmin(admin.ModelAdmin):
    pass

admin.site.register(TodoItem, TodoItemAdmin)
admin.site.register(DoneTodo, TodoItemAdmin)
