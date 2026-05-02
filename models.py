from django.db import models

class Profile(models.Model):
    user_name = models.CharField(max_length=50)

    def __str__(self):
        return self.user_name


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="posts"
    )

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:20]


class Tag(models.Model):
    name = models.CharField(max_length=30)
    posts = models.ManyToManyField(Post)

    def __str__(self):
        return self.name
