from django.contrib import admin

from .models import Department, IdDepartments, Services


def getFieldsModel(model):
    fields = [field.name for field in model._meta.get_fields() if
              field.many_to_many != True and field.one_to_many != True]
    return fields


class DepartmentAdmin(admin.ModelAdmin):
    list_display = getFieldsModel(Department)
    list_display_links = getFieldsModel(Department)


class IdDepartmensAdmin(admin.ModelAdmin):
    list_display = getFieldsModel(IdDepartments)
    list_display_links = getFieldsModel(IdDepartments)


class ServicesAdmin(admin.ModelAdmin):
    list_display = getFieldsModel(Services)
    list_display_links = getFieldsModel(Services)


admin.site.register(Department, DepartmentAdmin)
admin.site.register(IdDepartments, IdDepartmensAdmin)
admin.site.register(Services, ServicesAdmin)