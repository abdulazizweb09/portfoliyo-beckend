from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import (
    UserProfileViewSet,
    DeveloperViewSet,
    SkillViewSet,
    ToolViewSet,
    ProjectViewSet,
    BlogPostViewSet,
    ExperienceViewSet,
    EducationViewSet,
    MessageViewSet,
)


router = DefaultRouter()


router.register("profile", UserProfileViewSet, basename="profile")
router.register("developer", DeveloperViewSet, basename="developer")
router.register("skill", SkillViewSet, basename="skill")
router.register("tool", ToolViewSet, basename="tool")
router.register("project", ProjectViewSet, basename="project")
router.register("blog", BlogPostViewSet, basename="blog")
router.register("experience", ExperienceViewSet, basename="experience")
router.register("education", EducationViewSet, basename="education")
router.register("message", MessageViewSet, basename="message")


urlpatterns = router.urls