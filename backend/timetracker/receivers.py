from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import (
    pre_save, 
    post_save, 
    pre_delete, 
    post_delete, 
    pre_init, 
    post_init)
from rest_framework.authtoken.models import Token

UserModel = get_user_model()

@receiver(post_save, sender=UserModel)
def new_user_handler(sender, instance, created, **kwargs):
    if created:
        token = Token.objects.create(user=instance)
        print(token.key)