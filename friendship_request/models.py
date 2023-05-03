from django.db import models


class Friendship(models.Model):
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="user"
    )

    friend = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="friendship"
    )

    created_at = models.DateTimeField(auto_now_add=True)
