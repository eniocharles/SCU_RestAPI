from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

class UserManager(BaseUserManager):
    def create_user(self, email, nickname, password=None, **extra_fields):
        if not email:
            raise ValueError('O email é obrigatório')
        email = self.normalize_email(email)     #Normaliza o e-mail (minúsculas, etc.)
        user = self.model(email=email, nickname=nickname, **extra_fields)    
        user.set_password(password)     #Armazena de forma segura a senha
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)       #Superusuário faz parte da equipe
        extra_fields.setdefault('is_superuser', True)       #Superusuário tem todas as permissões
        return self.create_user(email, nickname, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, verbose_name='Email')
    nickname = models.CharField(max_length=20, unique=True, verbose_name='Nickname')
    password = models.CharField(max_length=128, verbose_name='Senha')       #Senha será hasheada
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')         #Usuário está ativo?
    is_staff = models.BooleanField(default=False, verbose_name='Equipe')        #Faz parte da equipe?

    objects = UserManager()

    USERNAME_FIELD = 'email'    # Campo usado para login
    REQUIRED_FIELDS = ['nickname']  # Campos obrigatórios ao criar um usuário


    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        ordering = ['-created_at']      #Ordena usuários por data de criação(do mais recente para o mais antigo)

    def __str__(self):
        return f'Nickname: {self.nickname} | Email: {self.email}'