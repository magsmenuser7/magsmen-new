from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from django.urls import reverse

# Create your models here.


class Category(models.Model):
        Name = models.CharField(max_length=30,default="heading")
        Created = models.DateTimeField(default=datetime.now)
        def __str__(self):
            return self.Name
        
        class Meta:
            verbose_name ='Category'
            verbose_name_plural = 'Categories'

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class BlogPost(models.Model):
    Id = models.AutoField(primary_key=True)
    Category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='categories')
    Title =  models.CharField(max_length=225,default="title")
    Description = models.CharField(max_length=2000,blank=True,null=True)
    Image1 = models.ImageField(upload_to='uploads/')
    Body = RichTextField(blank=True,null=True)
    Sluglink = models.CharField(max_length=200 ,blank=True,null=True)
    Tags = models.CharField(max_length=100 )
    CreatedName =  models.CharField(max_length=100)
    Create_at = models.DateTimeField(default=datetime.now)
    status = models.IntegerField(choices=STATUS, default=0)

    def get_absolute_url(self):
        return reverse('blog-details', args=[str(self.Sluglink)])

    class Meta:
        ordering = ['-Create_at']

    def __str__(self):
            return self.Title
    

class Media(models.Model):
    Id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=200)
    Slug = models.SlugField(max_length=300,blank=True,null=True)
    Url = models.URLField(max_length=300,default="",null=True)
    Image = models.ImageField(upload_to='uploads/')
    CreatedPaperName = models.CharField(max_length=100,null=True)
    CreatedAt = models.DateField(default=datetime.now)

    def __str__(self):
            return self.Title
    

class ContactData(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=254)
    Phone = models.CharField(max_length=10)
    Subject = models.CharField(max_length=100)
    Message = models.CharField(max_length=500)
    Date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.Name



Active_form =(
    (0,"active"),
    (1, "inactive")
)
class CareerInfo(models.Model):
    ExpertiseId = models.CharField(max_length=10,primary_key=True)
    ExpertiseName = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)
    CreatedAt = models.DateField(default=datetime.now)
    JobType = models.CharField(max_length=100)
    Description = models.CharField(max_length=1000)
    Body = RichTextField()
    Experience = models.CharField(max_length=50)
    WorkingHours = models.CharField(max_length=100)
    WorkingDays = models.CharField(max_length=50)
    Salary = models.CharField(max_length=50)
    Vacancy = models.IntegerField(default="")
    DeadLine = models.CharField(max_length=50)
    Sluglink = models.SlugField(unique=True, null=True)
    Active_status = models.IntegerField(choices=Active_form,default=1)

    def __str__(self):
        return self.ExpertiseName
    
    

class ApplyForm(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=50)
    Phone = models.CharField(max_length=10)
    SelectCategory = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)
    Uploadfile = models.FileField(upload_to='uploads/')
   

    def __str__(self):
         return self.Name
    

class StepformData(models.Model):
    Name = models.CharField(max_length=100,null=True)
    Email = models.EmailField(max_length=50,null=True)
    Phone = models.CharField(max_length=10,null=True)
    Brandmarketposition = models.CharField(max_length=100)
    BrandCorevalue = models.CharField(max_length=500)
    Brandperceive_targetaudience = models.CharField(max_length=100)
    CustomerFeedback = models.CharField(max_length=100)
    BrandPerformence = models.CharField(max_length=500)
    Challenges_Obstacles = models.CharField(max_length=500)
    Brand_Motivation = models.CharField(max_length=500)
    Goals_Achieves = models.CharField(max_length=500)
    Expectations = models.CharField(max_length=500)


    def __str__(self):
        return self.Name