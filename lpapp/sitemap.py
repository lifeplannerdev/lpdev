from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return ['home', 'about', 'service', 'germany', 'studycanada', 
                'studyeurope', 'contact', 'blog', 'careers', 'canada']

    def location(self, item):
        return reverse(f'lpapp:{item}')

    def lastmod(self, obj):
        # Return None if you don't track modifications
        return None