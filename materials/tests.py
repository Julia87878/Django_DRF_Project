from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Course, Lesson, Subscription
from users.models import CustomUser


class LessonAPITestCase(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(
            email="julie014@inbox.ru", username="Julie", password=749
        )
        self.course = Course.objects.create(name="Python", owner=self.user)
        self.lesson = Lesson.objects.create(
            name="Списки, их свойства в Python",
            course=self.course,
            owner=self.user,
            video_url="https://www.youtube.com/watch?v=eWRfhZUzrAc",
        )
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse("materials:lesson_retrieve", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.lesson.name)

    def test_lesson_create(self):
        url = reverse("materials:lesson_create")
        data = {
            "name": "Кортежи в Python",
            "course": 1,
            "video_url": "https://www.youtube.com/watch?v=cQfu-hYo2o4",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_lesson_update(self):
        url = reverse("materials:lesson_update", args=(self.lesson.pk,))
        data = {"video_url": "https://www.youtube.com/watch?v=cQfu-hYo2o4"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            data.get("video_url"), "https://www.youtube.com/watch?v=cQfu-hYo2o4"
        )

    def test_lesson_delete(self):
        url = reverse("materials:lesson_delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)

    def test_lesson_list(self):
        url = reverse("materials:lessons_list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "name": self.lesson.name,
                    "description": None,
                    "owner": self.user.pk,
                    "course": self.course.pk,
                    "image": None,
                    "video_url": self.lesson.video_url,
                }
            ],
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def test_subscription_create(self):
        self.assertEqual(Subscription.objects.count(), 0)
        url = reverse("materials:subscription_create_or_delete")
        data = {"id": self.course.pk}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "подписка добавлена")
        self.assertEqual(Subscription.objects.all().count(), 1)

    def test_subscription_delete(self):
        Subscription.objects.create(user=self.user, course=self.course)
        url = reverse("materials:subscription_create_or_delete")
        data = {"id": self.course.pk}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "подписка удалена")
        self.assertEqual(Subscription.objects.all().count(), 0)
