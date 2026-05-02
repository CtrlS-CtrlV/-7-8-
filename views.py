from .models import Post, Profile

def create_post():
    user = Profile.objects.create(user_name="Test")
    Post.objects.create(title="Post", content="Text", author=user)

def get_posts():
    return Post.objects.all()

def update_post(post_id):
    post = Post.objects.get(id=post_id)
    post.title = "Updated"
    post.save()

def delete_post(post_id):
    Post.objects.filter(id=post_id).delete()
