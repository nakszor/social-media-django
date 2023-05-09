from django.db import models


class Like(models.Model):
    post = models.ForeignKey("posts.Post", on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="i_liked")
    created_at = models.DateTimeField(auto_now_add=True)
