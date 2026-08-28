from rest_framework import serializers
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


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "avatar",
            "bio",
            "job",
            "resume",
            "location",
            "github",
            "linkedin",
            "website",
        ]


class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devoloper
        fields = [
            "id",
            "type",
        ]


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = [
            "id",
            "name",
            "is_active",
            "devoloper",
        ]


class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = [
            "id",
            "name",
            "is_active",
            "devoloper",
        ]


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "description",
            "image",
            "project_url",
            "git_hub",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "created_at",
        ]


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = [
            "id",
            "title",
            "content",
            "description",
            "image",
            "created_at",
            "updated_at",
            "is_published",
            "read_time",
            "slug",
            "views_count",
        ]

        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
            "slug",
            "views_count",
        ]


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = [
            "id",
            "job_title",
            "company",
            "start_date",
            "end_date",
            "description",
        ]


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = [
            "id",
            "school",
            "degree",
            "teacher",
            "start_year",
            "end_year",
            "description",
        ]


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = [
            "id",
            "name",
            "email",
            "phone",
            "subject",
            "message",
            "created_at",
            "is_read",
        ]

        read_only_fields = [
            "id",
            "created_at",
            "is_read",
        ]