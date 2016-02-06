from django.contrib import admin
from .models import Problem, Answer
#from .models import Exam

class AnswerInline(admin.TabularInline):
	model = Answer
	extra = 1

class ProblemAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['problem_text']})
	]
	inlines = [AnswerInline]
	list_display = ['problem_text']

"""class ExamAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['exam_name']}),
		('Date information', {'fields': ['pub_date']})
	]

class ExamAdmin(admin.ModelAdmin):
	fieldsets = [
		('Score Information', {'fields': ['score', 'num_problems']}),
	]

admin.site.register(Exam, ExamAdmin)"""
admin.site.register(Problem, ProblemAdmin)