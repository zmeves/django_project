from django.contrib.syndication.views import Feed
from django.urls import reverse
from blogging.models import Post


class LatestPostsFeed(Feed):
    title = "Recent Posts"
    link = '/postnews/'
    description = "Most recent posts on this website"

    def items(self):
        return Post.objects.order_by('-published_date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return f"{item.text}\nAuthor: {item.author}"

    def item_link(self, item):
        return reverse('blog_detail', args=[item.pk])
