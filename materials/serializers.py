from rest_framework import serializers

from materials.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["name", "description", "image"]


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ["name", "description", "course", "image", "video_url"]
