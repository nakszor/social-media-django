from django.db import models


class Follower(models.Model):
    followed = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="Im_following"
    )
    follower = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="my_followers"
    )
    created_at = models.DateTimeField(auto_now_add=True)
