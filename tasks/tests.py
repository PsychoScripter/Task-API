from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from tasks.models import Task

class TaskAPITestCase(APITestCase):
    def setUp(self):
        self.task = Task.objects.create(title="Test Task", description="Sample description")

    def test_list_tasks(self):
        url = reverse('task-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('title' in response.data[0])

    def test_add_task(self):
        url = reverse('task-add')
        data = {"title": "New Task", "description": "Some detail"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)

    def test_get_task_detail(self):
        url = reverse('task-detail', kwargs={'pk': self.task.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.task.title)
