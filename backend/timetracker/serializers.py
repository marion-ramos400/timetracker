from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Task

UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserModel
        fields = [
            "id",
            "username",
            "password"
        ]

    def create(self, validated_data):
        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        user.save()
        return user

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "id",
            "user",
            "start_dt",
            "hours",
            "description",
            "project"
        ]


    def create(self, validated_data):
        username = validated_data["user"]
        user = UserModel.objects.filter(username=username).first()
        if not user:
            #add handling here
            raise serializers.ValidationError(
                f"username: {username} not found"
            )

        task = Task.objects.create(
            user=user,
            start_dt=validated_data["start_dt"],
            hours=validated_data["hours"],
            description=validated_data["description"],
            project=validated_data["project"],
        )

        task.save()
        return task