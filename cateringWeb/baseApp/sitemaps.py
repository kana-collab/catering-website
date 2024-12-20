from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    # This sitemap is for a single page
    changefreq = "monthly"
    priority = 1.0

    def items(self):
        return ['homeclick']  # Reference to the 'home' URL

    def location(self, item):
        return reverse(item)  # Generate the URL for the 'home' page
