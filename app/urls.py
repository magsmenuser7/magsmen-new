from django.urls import path
from .views import home,about,expertise,brand_consulting,personal_brand_consulting,image_consulting,corporate_rebranding,brand_expresso,\
brand_creation,link_fluence,launchpad,blog,blogdetails,Ourmedia,Contact,Newsletter,Newslettertwo,Brand,Newsletterthree,BrandRefresh,DigitalTwin_BrandStrategy,\
works,telugufoods,suryacolors,tdhrishika,tenali_double_horse,triplex,vsb,zavaine,career,jobdetails,applyform,Questionsform,privacy_policy,faqs,terms_conditions,cancellation_and_refund_policy,\
Monochromatic_colors_in_branding,band_corner_the_new_age_of_buying_brand_activism,magsmen_brand_portfolio,brand_naming_unlock_the_soul_of_your_brand

from django.contrib.sitemaps.views import sitemap
from app.sitemap import PostSitemap,StaticPagesSitemap
from django.views.generic.base import TemplateView

sitemaps = {
    'posts': PostSitemap,
    'static_pages': StaticPagesSitemap,
}


urlpatterns = [
    path('', home, name="home"),
    path('about/',about,name="about"),
    path('expertise/',expertise,name="expertise"),
    path('brand-consulting/',brand_consulting,name="brand-consulting"),
    path('personal-brand-consulting/',personal_brand_consulting,name="personal-brand-consulting"),
    path('image-consulting/',image_consulting,name="image-consulting"),
    path('corporate-rebranding/',corporate_rebranding,name="corporate-rebranding"),
    path('brand-expresso/',brand_expresso,name="brand-expresso"),
    path('brand-creation/',brand_creation,name="brand-creation"),
    path('link-fluence/',link_fluence,name="link-fluence"),
    path('launchpad/',launchpad,name="launchpad"),
    path('blog/',blog,name="blog"),
    path('blog-details/<str:slug>',blogdetails,name="blog-details"),
    path('gallery/',Ourmedia,name='gallery'),
    path('works/',works,name="works"),
    path('telugufoods/',telugufoods,name="telugufoods"),
    path('suryacolors/',suryacolors,name="suryacolors"),
    path('tdhrishika/',tdhrishika,name="tdhrishika"),
    path('tenalidoublehorse/',tenali_double_horse,name="tenalidoublehorse"),
    path('triplex/',triplex,name="triplex"),
    path('vsb/',vsb,name="vsb"),
    path('zavaine/',zavaine,name="zavaine"),
    path('career/',career,name="career"),
    path('job-details/<str:slug>',jobdetails,name='jobdetails'),
    path('applyform/',applyform,name="applyform"),
    path('contact/',Contact,name="contact"),
    path('questions/', Questionsform , name='questions'),
    path('privacy-policy/', privacy_policy , name='privacy-policy'),
    path('terms-conditions/', terms_conditions , name='terms-conditions'),
    path('cancellation-refund-policy/', cancellation_and_refund_policy , name='cancellation-refund-policy'),
    path('faqs/', faqs, name='faqs'),
    path('magsmen-brand-portfolio/',magsmen_brand_portfolio,name='magsmen-brand-portfolio'),
    path('news-letter-august-2023/',Newsletter,name='news-letter-august-2023'),
    path('brand-architecture/',Brand,name='brand-architecture'),
    path('brand-corner-october-edition/',Newslettertwo,name='the-name-of-the-article-indian-brand-success-stories'),
    path('brand-corner-november-edition/',Newsletterthree,name='brand-corner-november-edition'), 
    path('brand-refresh-vs-rebranding/',BrandRefresh,name="brand-refresh-rebranding"),
    path('digital-twin-brand-strategy/',DigitalTwin_BrandStrategy,name="digital-twin-brand-strategy"),
    path('monochromatic-colors-in-branding/',Monochromatic_colors_in_branding,name="monochromatic-colors-in-branding"),
    path('the-new-age-of-buying-brand-activism/',band_corner_the_new_age_of_buying_brand_activism,name="the-new-age-of-buying-brand-activism"),
    path('brand-naming-unlock-the-soul-of-your-brand/',brand_naming_unlock_the_soul_of_your_brand,name="brand-naming-unlock-the-soul-of-your-brand"),
    path('sitemap.xml/',sitemap,{'sitemaps':sitemaps},name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt',TemplateView.as_view(template_name="uifiles/robots.txt", content_type="text/plain")),
   

]