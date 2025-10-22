from django.contrib import admin
from .models import BlogPost,Category,Media,ContactData,CareerInfo,ApplyForm,StepformData,Subscribe,IntalksForm,StrategySubmission

# Register your models here.

class AdminHappyCategories(admin.ModelAdmin):
    list_display=('Name','Created')


class AdminHappyBlogpost(admin.ModelAdmin):
    list_display=('Id','Category','Title','Tags','CreatedName','Create_at','status')
    list_filter = ["CreatedName",'Create_at']


class AdminMedia(admin.ModelAdmin):
    list_display = ['Title','Image','Slug']
    

class AdminHappyContact(admin.ModelAdmin):
    list_display=('Name','Email','Phone','Subject','Message')


class AdminCareerInfo(admin.ModelAdmin):
    list_display = ['ExpertiseName','Location','CreatedAt']


class AdminApplyForm(admin.ModelAdmin):
    list_display=['Name','Email','Phone']


class AdminStepformData(admin.ModelAdmin):
    list_display = ['name','email','phone','Brandmarketposition','BrandCorevalue','Brandperceive_targetaudience','CustomerFeedback','BrandPerformence','Challenges_Obstacles']


class AdminSubscribe(admin.ModelAdmin):
    list_display = ('Email',)

class AdminIntalksForm(admin.ModelAdmin):
    list_display = ['id','Name','Email','Contact','City','Reason_to_connect']


class StrategySubmissionAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'email',
        'phone_number',
        'location',
        'q1_answer',
        'q2_answer',
        'q3_answer',
        'submitted_at',
    )
    search_fields = ('full_name', 'email', 'phone_number', 'location', 'q1_answer', 'q2_answer', 'q3_answer')
    list_filter = ('submitted_at', 'location')
    readonly_fields = ('submitted_at',)
    ordering = ('-submitted_at',)



admin.site.register(Category,AdminHappyCategories)
admin.site.register(BlogPost,AdminHappyBlogpost)
admin.site.register(Media,AdminMedia)
admin.site.register(ContactData,AdminHappyContact)
admin.site.register(CareerInfo,AdminCareerInfo)
admin.site.register(ApplyForm,AdminApplyForm)
admin.site.register(StepformData,AdminStepformData)
admin.site.register(Subscribe,AdminSubscribe)
admin.site.register(IntalksForm,AdminIntalksForm)
admin.site.register(StrategySubmission,StrategySubmissionAdmin)