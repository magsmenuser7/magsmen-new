from django.contrib.sitemaps import Sitemap,GenericSitemap
from .models import BlogPost
from django.urls import reverse


class StaticPagesSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return ['about', 'services', 'brand-consulting', 'personal-brand-consulting', 'image-consulting', 'corporate-rebranding', 'brand-expresso', 'brand-creation','launchpad','gallery','works','contact']

    def location(self, item):
        return reverse(item)


class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9
    
    def items(self):
         return BlogPost.objects.filter(status=1)
    
    def lastmod(self,obj):
        return obj.Create_at
