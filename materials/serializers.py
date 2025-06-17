from rest_framework import serializers

from materials.models import Course, Lesson, Subscription
from materials.validators import UrlCustomValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ["name", "description", "owner", "course", "image", "video_url"]
        validators = [UrlCustomValidator(field="video_url")]


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)
    active_subscription = serializers.SerializerMethodField(read_only=True)

    def get_lesson_count(self, obj):
        return obj.lessons.count()

    def get_active_subscription(self, obj):
        request = self.context.get("request")
        return Subscription.objects.filter(user=request.user, course=obj).exists()

    class Meta:
        model = Course
        fields = "__all__"


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"
