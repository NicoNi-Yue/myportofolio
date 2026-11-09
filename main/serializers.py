from django.utils.html import strip_tags
from rest_framework import serializers

from main.models import Education, Experience, Project


class CleanTextModelSerializer(serializers.ModelSerializer):
    text_fields = ()

    def validate(self, attrs):
        attrs = super().validate(attrs)
        for field in self.text_fields:
            if field in attrs and isinstance(attrs[field], str):
                cleaned = strip_tags(attrs[field]).strip()
                if field == "title" and not cleaned:
                    raise serializers.ValidationError({field: "This field may not be blank."})
                attrs[field] = cleaned
        return attrs


class ProjectSerializer(CleanTextModelSerializer):
    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()
    starred_by_names = serializers.SerializerMethodField()
    text_fields = ("title", "description", "tech_stack")

    class Meta:
        model = Project
        fields = ["id", "title", "description", "tech_stack", "project_url",
                  "project_image_url", "star_count", "is_starred", "starred_by_names"]
        read_only_fields = ["id", "star_count", "is_starred", "starred_by_names"]

    def get_star_count(self, obj):
        return obj.starred_by.count()

    def get_is_starred(self, obj):
        request = self.context.get("request")
        return bool(request and request.user.is_authenticated and obj.starred_by.filter(pk=request.user.pk).exists())

    def get_starred_by_names(self, obj):
        return ", ".join(obj.starred_by.values_list("username", flat=True))


class ExperienceSerializer(CleanTextModelSerializer):
    is_ongoing = serializers.ReadOnlyField()
    category_display = serializers.CharField(source="get_category_display", read_only=True)
    text_fields = ("title", "description")

    class Meta:
        model = Experience
        fields = ["id", "title", "description", "category", "category_display",
                  "thumbnail", "started_at", "ended_at", "is_ongoing"]
        read_only_fields = ["id", "category_display", "is_ongoing"]


class EducationSerializer(CleanTextModelSerializer):
    is_ongoing = serializers.ReadOnlyField()
    category_display = serializers.CharField(source="get_category_display", read_only=True)
    text_fields = ("title", "description")

    class Meta:
        model = Education
        fields = ["id", "title", "description", "category", "category_display",
                  "logo", "started_at", "ended_at", "is_ongoing"]
        read_only_fields = ["id", "category_display", "is_ongoing"]
