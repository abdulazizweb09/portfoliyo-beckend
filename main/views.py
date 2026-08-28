from rest_framework.viewsets import ModelViewSet

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

from .serializers import (
    UserProfileSerializer,
    DeveloperSerializer,
    SkillSerializer,
    ToolSerializer,
    ProjectSerializer,
    BlogPostSerializer,
    ExperienceSerializer,
    EducationSerializer,
    MessageSerializer,
)


class UserProfileViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class DeveloperViewSet(ModelViewSet):
    queryset = Devoloper.objects.all()
    serializer_class = DeveloperSerializer


class SkillViewSet(ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class ToolViewSet(ModelViewSet):
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class BlogPostViewSet(ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


class ExperienceViewSet(ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class EducationViewSet(ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer