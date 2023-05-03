from django.db import models


class Friend(models.Model):
    friend = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="friends"
    )

    created_at = models.DateTimeField(auto_now_add=True)
