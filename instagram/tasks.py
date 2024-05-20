from celery import shared_task
from .models import Post
from playwright_engine.sync_instagram.instagram import Instagram


@shared_task
def create_publication(post_id):
    post = Post.objects.get(id=post_id)
    Instagram.create_publication(post)
    post.published = True
    post.save()