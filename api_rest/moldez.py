from django.db import models

class User(models.Model):
    user_id = models.IntegerField()
    user_nickname = models.CharField(max_length=20)
    user_email = models.EmailField(unique=True)
    user_password = models.CharField(max_length=50)
    user_created_at = models.DateTimeField(auto_now_add=True)
    user_updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("user")
        verbose_name_plural = ("users")

    def __str__(self):
        return f'Nickname: {self.nickname} | Email: {self.email1}'

