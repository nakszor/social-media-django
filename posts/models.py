from django.db import models


class PrivacyOptions(models.TextChoices):
    public_privacy = "Public"
    private_privacy = "Private"
    friends_privacy = "Friends"


class Post(models.Model):
    title = models.CharField(max_length=50, unique=True)
    content = models.TextField()
    privacy = models.CharField(
        choices=PrivacyOptions.choices, default=PrivacyOptions.public_privacy
    )
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="posts",
    )

    def __str__(self) -> str:
        return f"<Post [{self.id}] - [{self.title}]>"
