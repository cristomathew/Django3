from import_export.admin import ImportExportModelAdmin
from import_export import resources
from django.contrib import admin
from .models import Questions
# Register your models here.
class QuestionResource(resources.ModelResource):
    class Meta:
        model = Questions
class QuestionAdmin(ImportExportModelAdmin):
    resource_class = QuestionResource
admin.site.register(Questions, QuestionAdmin)
