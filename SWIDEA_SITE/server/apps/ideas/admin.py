from django.contrib import admin
from .models import Idea, Devtool
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class IdeaResource(resources.ModelResource):
	class Meta:
		model = Idea
		fields = ('id', 'title', 'image', 'content', 'interest', 'devtool')

class IdeaAdmin(ImportExportModelAdmin):
	fields = ('title', 'image', 'content', 'interest', 'devtool')
    #상세페이지 설명
	list_display = ('id', 'title', 'image', 'content', 'interest', 'devtool')
    #바깥 페이지에서 보일 부분 정
	resource_class = IdeaResource

# admin.site.register(Idea, IdeaAdmin)
admin.site.register(Idea)
admin.site.register(Devtool)