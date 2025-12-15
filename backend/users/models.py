from django.db import models
from django.contrib.auth.models import AbstractUser
# импортируем абстракт user уже подразумеваем готовой моделью что у нас есть стандартные поля регистрации пользователя
# значит создаем просто класс пользователь с обычными полями не регистрационными

class User(AbstractUser):
    phone = models.CharField(max_length=12)
    post = models.EmailField()
    create_at = models.DateTimeField(auto_now_add=True)