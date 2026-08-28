from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import (
    UserProfile,
    Devoloper,
    Skill,
    Tool,
    Project,
    BlogPost,
    Experience,
    Education,
    Message,
)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "username",
        "email",
        "first_name",
        "last_name",
        "job",
        "location",
        "is_active",
    )

    search_fields = (
        "username",
        "email",
        "first_name",
        "last_name",
        "job",
    )

    list_filter = (
        "is_active",
        "is_staff",
    )


@admin.register(Devoloper)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "type",
    )

    list_filter = (
        "type",
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "devoloper",
        "is_active",
    )

    search_fields = (
        "name",
    )

    list_filter = (
        "is_active",
        "devoloper",
    )


@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "devoloper",
        "is_active",
    )

    search_fields = (
        "name",
    )

    list_filter = (
        "is_active",
        "devoloper",
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "project_url",
        "git_hub",
        "created_at",
    )

    search_fields = (
        "title",
        "description",
    )

    list_filter = (
        "created_at",
    )

    readonly_fields = (
        "created_at",
    )


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "is_published",
        "read_time",
        "created_at",
        "updated_at",
    )

    search_fields = (
        "title",
        "description",
        "content",
    )

    list_filter = (
        "is_published",
        "created_at",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
        "views_count",
    )

    prepopulated_fields = {
        "slug": ("title",),
    }


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "job_title",
        "company",
        "start_date",
        "end_date",
    )

    search_fields = (
        "job_title",
        "company",
    )

    list_filter = (
        "company",
        "start_date",
    )


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "school",
        "degree",
        "teacher",
        "start_year",
        "end_year",
    )

    search_fields = (
        "school",
        "degree",
        "teacher",
    )

    list_filter = (
        "school",
        "start_year",
    )


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "email",
        "phone",
        "subject",
        "is_read",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "subject",
        "message",
    )

    list_filter = (
        "is_read",
        "created_at",
    )

    readonly_fields = (
        "created_at",
    )