from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import User

class UserTests(APITestCase):
    def setUp(self):
        # Cria um usuário para testes
        self.user = User.objects.create_user(
            email="test@example.com",
            nickname="testuser",
            password="testpassword"
        )

    def test_user_registration(self):
        url = reverse('register')
        data = {
            "email": "newuser@example.com",
            "nickname": "newuser",
            "password": "newpassword"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)  # Verifica se o usuário foi criado

    def test_user_login(self):
        url = reverse('login')
        data = {
            "email": "test@example.com",
            "password": "testpassword"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)  # Verifica se o token foi retornado

    def test_user_list(self):
        url = reverse('user-list')
        # Autentica o usuário
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Verifica se o usuário está na lista

    def test_user_detail(self):
        url = reverse('user-detail', args=[self.user.id])
        # Autentica o usuário
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nickname'], 'testuser')  # Verifica os detalhes do usuário

    def test_user_update(self):
        url = reverse('user-detail', args=[self.user.id])
        # Autentica o usuário
        self.client.force_authenticate(user=self.user)
        data = {
            "nickname": "updateduser",
            "email": "updated@example.com"
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.nickname, 'updateduser')  # Verifica se o nickname foi atualizado

    def test_user_delete(self):
        url = reverse('user-detail', args=[self.user.id])
        # Autentica o usuário
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.count(), 0)  # Verifica se o usuário foi excluído