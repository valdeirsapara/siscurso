from django.test import TestCase
from django.contrib.auth.models import User

class LoginTestCase(TestCase):
    def setUp(self):
        # Cria um usuário para o teste
        self.username = "testuser"
        self.password = "testpassword"
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_login_success(self):
        # Tenta fazer login com credenciais corretas
        response = self.client.post('/login/', {'username': self.username, 'password': self.password})
        self.assertEqual(response.status_code, 200)  # Verifica se o login foi bem-sucedido
        self.assertContains(response, "Bem-vindo")  # Verifica se a mensagem de boas-vindas aparece

    def test_login_failure(self):
        # Tenta fazer login com credenciais incorretas
        response = self.client.post('/login/', {'username': self.username, 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 401)  # Verifica se o login falhou
        self.assertContains(response, "Credenciais inválidas")  # Verifica se a mensagem de erro aparece
