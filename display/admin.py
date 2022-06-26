from django.contrib import admin
from display.models import Profile
from django.contrib.auth.admin import UserAdmin
from display.models import About
from display.models import Skill, Project, SchoolProject, Education, Education_tran
from display.models import Project
from display.models import SchoolProject
from display.models import Education
from display.models import Education_tran
# Register your models here.


class AboutAdmin(admin.ModelAdmin):
    list_display = ["about", "conclusion", "dob", "nation", "phone", "profession", "email", "github", "leet", "linked", "graduate", "nation_url"]

class SkillAdmin(admin.ModelAdmin):
    list_display = [
        "language_proficient",
        "language_familiar",
        "backend",
        "frontend",
        "tools",
        "api"]


class ProjectAdmin(admin.ModelAdmin):
    list_display = ["title", "image", "uses", "description", "schoolp", "url", "source_code", "image2", "image3", "image4", "date"]


class SchoolProjectAdmin(admin.ModelAdmin):
    list_display = ["title", "image", "uses", "description"]


class EducationAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "date", "total_date", "gpa"]


class Education_tranAdmin(admin.ModelAdmin):
    list_display = ["image", "title", "url"]

admin.site.register(Profile)
admin.site.register(About, AboutAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(SchoolProject, SchoolProjectAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Education_tran, Education_tranAdmin)