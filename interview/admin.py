from django.contrib import admin

from interview.models import Candidate
# Register your models here.


class CandidateAdmin(admin.ModelAdmin):
    # 不需要展示
    exclude = ('creator', 'created_date', 'modified_date')

    list_display = (
            'username', 'city', 'bachelor_school', 'first_score', 'first_result', 'first_interviewer',
            'second_result', 'second_interviewer', 'hr_score', 'hr_result', 'last_editor'
    )


admin.site.register(Candidate, CandidateAdmin)
