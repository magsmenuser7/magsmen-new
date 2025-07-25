from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import BlogPost

class StaticPagesSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return [
            'home',
            'about', 'expertise', 'brand-consulting', 'personal-brand-consulting',
            'image-consulting', 'corporate-rebranding', 'brand-expresso',
            'brand-creation', 'launchpad', 'gallery', 'works', 'contact'
        ]

    def location(self, item):
        return reverse(item)

    def get_urls(self, site=None, **kwargs):
        from django.contrib.sites.models import Site
        site = Site(domain="magsmen.com", name="Magsmen")
        return super().get_urls(site=site, **kwargs)


class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return BlogPost.objects.filter(status=1)

    def lastmod(self, obj):
        return obj.Create_at

    def location(self, obj):
        return f"/blog-details/{obj.Sluglink}/"  # adjust as needed

    def get_urls(self, site=None, **kwargs):
        from django.contrib.sites.models import Site
        site = Site(domain="magsmen.com", name="Magsmen")
        return super().get_urls(site=site, **kwargs)














# from django.contrib.sitemaps import Sitemap,GenericSitemap
# from .models import BlogPost
# from django.urls import reverse


# class StaticPagesSitemap(Sitemap):
#     changefreq = 'weekly'
#     priority = 0.8

#     def items(self):
#         return ['about', 'expertise', 'brand-consulting', 'personal-brand-consulting', 'image-consulting', 'corporate-rebranding', 'brand-expresso', 'brand-creation','launchpad','gallery','works','contact']

#     def location(self, item):
#         return reverse(item)


# class PostSitemap(Sitemap):
#     changefreq = 'weekly'
#     priority = 0.9
    
#     def items(self):
#          return BlogPost.objects.filter(status=1)
    
#     def lastmod(self,obj):
#         return obj.Create_at
