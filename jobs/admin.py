from django.contrib import admin
from jobs.models import Job

# Register your models here.


class JobAdmin(admin.ModelAdmin):
	# 隐藏
	exclude = ('creator', 'created_date', 'modified_date')
	# 展现
	list_display = ('job_name', 'job_type', 'job_city', 'creator', 'created_date', 'modified_date')

	# 保存一个模型之前进行操作(把当前登陆用户设为创建人)
	def save_model(self, request, obj, form, change):
		obj.creator = request.user
		super().save_model(request, obj, form, change)


admin.site.register(Job, JobAdmin)
