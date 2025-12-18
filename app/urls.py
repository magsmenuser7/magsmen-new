from django.urls import path
from .views import home,about,expertise,brand_consulting,personal_brand_consulting,image_consulting,corporate_rebranding,brand_expresso,\
brand_creation,link_fluence,launchpad,blog,blogdetails,Ourmedia,Contact,Newsletter,Newslettertwo,Brand,Newsletterthree,BrandRefresh,DigitalTwin_BrandStrategy,\
works,telugufoods,suryacolors,tdhrishika,tenali_double_horse,triplex,vsb,zavaine,career,jobdetails,applyform,Questionsform,privacy_policy,faqs,terms_conditions,cancellation_and_refund_policy,\
Monochromatic_colors_in_branding,band_corner_the_new_age_of_buying_brand_activism,magsmen_brand_portfolio,brand_naming_unlock_the_soul_of_your_brand,the_power_of_consistency_why_brand_tone_matters,\
a_cutting_edge_approach_in_branding_compressed,quiet_branding_silence_that_speaks_volumes,the_raise_ofreferral_marketing_growth_strategy_or_grey_zone,brandauditsystem,otc_purple,glocalization_where_global_meets_local,\
festive_commerce_why_navratri_is_the_new_brand_battleground,the_bottled_water_is_not_just_hydrating_it_is_transforming,submit_strategy,tdhproteindashboard,delhiworldschoolbrandhealthinfographic,brandaudit,\
brandaudit_sreenidhiglobalschoolaudit,delhiworldschool_brandanddigitalaudit,tdh_product_communication_Analysis,tdh_group_strategic_dashboard,tdh_x_pure_o_natural,brand_detox,sowmya_feeds,client_version_garthapuri,\
infinite_andhra_strategic_tourismb_lueprint,andhra_pradesh_aviation_network

from .views import *

from django.contrib.sitemaps.views import sitemap
from app.sitemap import PostSitemap,StaticPagesSitemap
from django.views.generic.base import TemplateView
from .views import contact_api_view,get_contacts

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
    path('puzzle/', submit_strategy, name='puzzle'),
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
    path('the-power-of-consistency-why-brand-tone-matters/',the_power_of_consistency_why_brand_tone_matters,name="the-power-of-consistency-why-brand-tone-matters"),
    path('a-cutting-edge-approach-in-branding/',a_cutting_edge_approach_in_branding_compressed,name="a-cutting-edge-approach-in-branding"),
    path('sitemap.xml/',sitemap,{'sitemaps':sitemaps},name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt',TemplateView.as_view(template_name="uifiles/robots.txt", content_type="text/plain")),
    path('api/contact/', contact_api_view, name='contact-api'),
    path('api/getcontact/',get_contacts, name='getcontact-api'),
    path('brand_corner_trademarks_and_deceptive_practices/',brand_corner_news_letter, name='brand_corner_trademarks_and_deceptive_practices'),
    path('beyond-the-logo-More-Than-a-Mark-Its-a-Movement/',brand_corner_beyond_the_logonews_letter, name='beyond-the-logo-More-Than-a-Mark-Its-a-Movement'),
    path('brand-corner-beyond-single-use/',brand_corner_beyond_single_use, name='brand-corner-beyond-single-use'),
    path('brand_corner_ethical_branding/',brand_corner_ethical_branding, name='brand_corner_ethical_branding'),
    path('quiet-branding-silence-that-speaks-volumes/',quiet_branding_silence_that_speaks_volumes, name='quiet-branding-silence-that-speaks-volumes'),
    path('the-raise-ofreferral-marketing-growth-strategy-or-grey-zone/',the_raise_ofreferral_marketing_growth_strategy_or_grey_zone, name='the-raise-ofreferral-marketing-growth-strategy-or-grey-zone'),
    path('glocalization-where-global-meets-local/', glocalization_where_global_meets_local, name='glocalization-where-global-meets-local'),
    path('festive-commerce-why-navratri-is-the-new-brand-battleground/', festive_commerce_why_navratri_is_the_new_brand_battleground, name='festive-commerce-why-navratri-is-the-new-brand-battleground'),
    path('the-bottled-water-is-not-just-hydrating-it-is-transforming/', the_bottled_water_is_not_just_hydrating_it_is_transforming, name='the-bottled-water-is-not-just-hydrating-it-is-transforming'),
    path('brand-corner-brand-detox/',brand_detox, name='brand-corner-brand-detox'),
    path('brandauditsystem/', brandauditsystem, name='brandauditsystem'),
    path('one-time-consulting/', otc_purple, name='one-time-consulting'),
    path('tdh-protein-market-opportunity/', tdhproteindashboard, name='tdh-protein-market-opportunity'),
    path('tdh-product-communication-Analysis/', tdh_product_communication_Analysis, name='tdh-product-communication-Analysis'),
    path('tdh-group-strategic-dashboard/', tdh_group_strategic_dashboard, name='tdh-group-strategic-dashboard'),
    path('delhi-world-school-brand-health-infographic/', delhiworldschoolbrandhealthinfographic, name='delhi-world-school-brand-health-infographic'),
    path('brand-audit/', brandaudit, name='brand-audit'),
    path('brand-audit-sreenidhi-global-school-audit/', brandaudit_sreenidhiglobalschoolaudit, name='brand-audit-sreenidhi-global-school-audit'),
    path('delhi-world-school-brand-and-digital-audit/', delhiworldschool_brandanddigitalaudit, name='delhi-world-school-brand-and-digital-audit'),
    path('tdh-x-pure-o-natural/', tdh_x_pure_o_natural, name='tdh-x-pure-o-natural'),
    path('sowmya-feeds/', sowmya_feeds, name='sowmya-feeds'),
    path('garthapuri/', client_version_garthapuri, name='garthapuri'),
    path('infinite-andhra-strategic-tourism-blueprint/', infinite_andhra_strategic_tourismb_lueprint, name='infinite-andhra-strategic-tourism-blueprint'),
    path('andhra-pradesh-aviation-network/', andhra_pradesh_aviation_network, name='andhra-pradesh-aviation-network'),



]