import json
import os
from urllib import request
from django.http import FileResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render

from magsmen import settings
from .models import BlogPost,Media,ContactData,CareerInfo,ApplyForm,StepformData,Subscribe
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.mail import send_mail,EmailMessage
from django.contrib import messages

# Create your views here.

def home(request):
    blog_list = BlogPost.objects.filter().order_by('-Id')[:3]    #filter(status=1).order_by('Create_at')

    if request.method == "POST":
        email = request.POST.get('email')

        if email:  # Check if the email field is not empty
            if Subscribe.objects.filter(Email=email).exists():
                # Return an error response if email already exists
                return HttpResponseRedirect('/?error=You are already subscribed')
            
            try:
                # Save to the database
                Subscribe.objects.create(Email=email)

                send_mail(
                    subject='Subscription Confirmation',
                    message='Thank you for subscribing, you will get notifications soon',
                    from_email='connectmagsmen@gmail.com',
                    recipient_list=[email],
                    fail_silently=False,
                )

                # Return a success response
                return HttpResponseRedirect('/?success=Subscription successful! Check your email for confirmation.')
            
            except Exception as e:
                # Handle unexpected errors
                return HttpResponseRedirect('/?error=An error occurred. Please try again.')
        else:
            # Return an error response if email is empty
            return HttpResponseRedirect('/?error=Email field cannot be empty.')

    return render(request, 'uifiles/home-two.html',{'blog_list':blog_list})

def about(request):
    return render(request, 'uifiles/about.html')

def expertise(request):
    return render(request, 'uifiles/services.html')

def brand_consulting(request):
    return render(request, 'uifiles/brand-consulting.html')

def personal_brand_consulting(request):
    return render(request, 'uifiles/personal-brand-consulting.html')

def image_consulting(request):
    return render(request, 'uifiles/image-consulting.html')

def corporate_rebranding(request):
    return render(request, 'uifiles/corporate-rebranding.html')

def brand_expresso(request):
    return render(request, 'uifiles/brand-expresso.html')

def brand_creation(request):
    return render(request, 'uifiles/brand-creation.html')

def link_fluence(request):
    return render(request, 'uifiles/linkfluence.html')

def launchpad(request):
    return render(request, 'uifiles/launchpad.html')

def blog(request):
    blog_list = BlogPost.objects.filter().order_by('-Id')
    paginator = Paginator(blog_list, 9) # paginate 10 posts per page
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'uifiles/blog.html',{'blog_list':posts,'posts':posts,'page':page})

def blogdetails(request,slug):
    blogpost = BlogPost.objects.get(Sluglink=slug)
    return render(request, 'uifiles/blog-details.html',{'blogpost':blogpost})

def Ourmedia(request):
    media = Media.objects.filter().order_by('-Id')
    paginator = Paginator(media,9)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,'uifiles/media.html',{'media':posts,'posts':posts,'page':page})

def works(request):
    return render(request, 'uifiles/works.html')

def telugufoods(request):
    return render(request, 'uifiles/telugu-foods.html')

def suryacolors(request):
    return render(request, 'uifiles/surya-colors.html')

def tdhrishika(request):
    return render(request, 'uifiles/tdhrishika.html')

def tenali_double_horse(request):
    return render(request, 'uifiles/tenali-double-horse.html')

def triplex(request):
    return render(request, 'uifiles/triplex.html')

def vsb(request):
    return render(request, 'uifiles/vsb.html')

def zavaine(request):
    return render(request, 'uifiles/zavaine.html')

def career(request):
    career_job = CareerInfo.objects.all()
    return render(request, 'uifiles/career.html',{'career_job':career_job})

def jobdetails(request,slug):
    career_job = CareerInfo.objects.get(Sluglink=slug)
    return render(request, 'uifiles/jobdetails.html',{'career_job':career_job})

def applyform(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phonenumber')
        selectcategory = request.POST.get('selectcategory')
        location = request.POST.get('location')
        file = request.FILES.get('file')

        oApplyformdata = ApplyForm(Name=name,Email=email,Phone=phone,SelectCategory=selectcategory,Location=location,Uploadfile=file)
        oApplyformdata.save()

        subject = 'Job Notification: {}'.format(name)
        message = '''
        New Job Notification:

        Name: {}
        Email: {}
        Phone Number: {}
        Selected Category: {}
        Location: {}

        '''.format(name, email, phone, selectcategory, location)

        email_from = 'connectmagsmen@gmail.com'
        recipient_list = ['connectmagsmen@gmail.com', ]
        send_mail(subject, message, 'connectmagsmen@gmail.com', recipient_list=['connectmagsmen@gmail.com'])

        return JsonResponse({'success': True})
    return render(request, 'uifiles/applyform.html')



def Contact(request):
    if request.method == "POST":
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        phone = request.POST.get('phone',"")
        subject = request.POST.get('subject',"")
        message = request.POST.get('message',"")
        oContactinfo = ContactData(Name=name,Email=email,Phone=phone,Subject=subject,Message=message)
        oContactinfo.save()
        
        message ='''
        Name:{}
        Email:{}
        Phone:{}
        Subject:{}
        Message:{}
        From:{}
        '''.format(name,email,phone,subject,message,email)
        try:
            send_mail(subject, message,'connectmagsmen@gmail.com',recipient_list=['connectmagsmen@gmail.com']) 
            messages.success(request,'Message has been sucesfully send')
        except:
            messages.error(request,'Your message has been failed, Please Try Agian')
    return render(request, 'uifiles/contact.html')



def Questionsform(request):
    if request.method == 'POST':
        storedFormData = request.POST.get('storedFormData')
        
        # Convert JSON string to dictionary
        stored_form_data = json.loads(storedFormData)
        
        # name=request.POST.get('name')
        # email=request.POST.get('email')
        # phone=request.POST.get('phone')
        # storedFormData = request.POST.get('storedFormData')
        brandposition = request.POST.get('brandposition')
        corevalue = request.POST.get('corevalue')
        brandtarget = request.POST.get('brandtarget')
        customerfeedback = request.POST.get('customerfeedback')
        brandperform = request.POST.get('brandperform')
        brandchallenge = request.POST.get('brandchallenge')
        brandmotivation = request.POST.getlist('brandcheck')
        achieve = request.POST.get('achieve')
        brandexpectation = request.POST.get('brandexpectation')

        oQuestion_data = StepformData(name=stored_form_data.get('fname'),email=stored_form_data.get('femail'),phone=stored_form_data.get('fphone'),Brandmarketposition=brandposition,BrandCorevalue=corevalue,Brandperceive_targetaudience=brandtarget,CustomerFeedback=customerfeedback,BrandPerformence=brandperform,Challenges_Obstacles=brandchallenge,Brand_Motivation=brandmotivation,Goals_Achieves=achieve,Expectations=brandexpectation)
        oQuestion_data.save()
        
         # Send email notification
        subject = 'Step Form Submission Notification'
        message = 'A form has been submitted with the following details:\n\n' \
                  f'Name: {stored_form_data.get("fname")}\n' \
                  f'Email: {stored_form_data.get("femail")}\n' \
                  f'Phone: {stored_form_data.get("fphone")}\n\n' \
                  'Additional form details:\n' \
                  f'Brand Position: {brandposition}\n' \
                  f'Core Value: {corevalue}\n' \
                  f'Target Audience: {brandtarget}\n' \
                  f'Customer Feedback: {customerfeedback}\n' \
                  f'Brand Performance: {brandperform}\n' \
                  f'Brand Challenge: {brandchallenge}\n' \
                  f'Brand Motivation: {", ".join(brandmotivation)}\n' \
                  f'Achievements: {achieve}\n' \
                  f'Brand Expectation: {brandexpectation}'
        
        from_email = 'connectmagsmen@gmail.com'  # Update with your sender email
        to_email = ['connectmagsmen@gmail.com']  # Update with recipient email(s)
        
        try:
            send_mail(subject, message,'connectmagsmen@gmail.com', recipient_list=['connectmagsmen@gmail.com'])
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    
    return render(request, 'uifiles/multistepform.html')


def privacy_policy(request):
    return render(request,'uifiles/privacy-policy-two.html')

def terms_conditions(request):
    return render(request,'uifiles/terms-conditions.html')

def cancellation_and_refund_policy(request):
    return render(request,'uifiles/cancellation-and-refund-policy.html')

def faqs(request):
    return render(request,'uifiles/faqs.html')

def handler404(requerst, exception):
    return render(requerst, 'uifiles/404.html',status=400)

def magsmen_brand_portfolio(request):
   
    pdf_filename = 'magsmen-brand-portfolio.pdf'
    pdf_path = os.path.join(settings.MEDIA_ROOT, pdf_filename)
    
    response = FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="{pdf_filename}"'
    return response


def Newsletter(request):
   
    pdf_filename = 'news-letter-august-2023.pdf'
    pdf_path = os.path.join(settings.MEDIA_ROOT, pdf_filename)
    
    response = FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="{pdf_filename}"'
    return response

def Newslettertwo(request):
    pdf_filename_two = 'the-name-of-the-article-indian-brand-success-stories.pdf'
    pdf_path = os.path.join(settings.MEDIA_ROOT, pdf_filename_two)
    
    response = FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="{pdf_filename_two}"'
    return response

def Newsletterthree(request):
    pdf_filename_two = 'brand-corner-november-edition.pdf'
    pdf_path = os.path.join(settings.MEDIA_ROOT, pdf_filename_two)
    
    response = FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="{pdf_filename_two}"'
    return response

def Brand(request):
    pdf_filename_three = 'brand-architecture.pdf'
    pdf_path = os.path.join(settings.MEDIA_ROOT, pdf_filename_three)
    
    response = FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="{pdf_filename_three}"'
    return response


def BrandRefresh(request):
    pdf_filename_four = 'brand-refresh-rebranding-june.pdf'
    pdf_path = os.path.join(settings.MEDIA_ROOT, pdf_filename_four)
    
    response = FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="{pdf_filename_four}"'
    return response


def DigitalTwin_BrandStrategy(request):
    pdf_filename_five = 'digital-twin-brand-strategy.pdf'
    pdf_path = os.path.join(settings.MEDIA_ROOT, pdf_filename_five)
    
    response = FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="{pdf_filename_five}"'
    return response


def Monochromatic_colors_in_branding(request):
    pdf_filename_six = 'monochromatic-colors-in-branding.pdf'
    pdf_path = os.path.join(settings.MEDIA_ROOT, pdf_filename_six)
    
    response = FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="{pdf_filename_six}"'
    return response

def band_corner_the_new_age_of_buying_brand_activism(request):
    pdf_filename_seven = 'band-corner-the-new-age-of-buying-brand-activism.pdf'
    pdf_path = os.path.join(settings.MEDIA_ROOT, pdf_filename_seven)
    
    response = FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="{pdf_filename_seven}"'
    return response

def brand_naming_unlock_the_soul_of_your_brand(request):
    pdf_filename_eight = 'brand-naming-unlock-the-soul-of-your-brand.pdf'
    pdf_path = os.path.join(settings.MEDIA_ROOT, pdf_filename_eight)
    
    response = FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="{pdf_filename_eight}"'
    return response