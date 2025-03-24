from django.http import JsonResponse
from django.shortcuts import render,redirect
from .forms import AppointmentForm,WebinarForm  
from .models import Team,Appointment,Immigration,JobApplication
from .forms import TeamForm,ReviewForm
from .models import Team, Review
from django.contrib import messages
from .models import Careers
import json
from .forms import CareersForm
from .models import JobApplication
from django.shortcuts import get_object_or_404
from django.views.decorators.cache import cache_page

# @cache_page(300)  
def home(request):
    if request.method == 'POST':
        # Check if the form submission is for the AppointmentForm
        if 'firstname' in request.POST:
            appointment_form = AppointmentForm(request.POST)
            if appointment_form.is_valid():
                appointment_form.save()
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'error': appointment_form.errors.as_json()})
        
        # Check if the form submission is for the EnrollmentForm
        elif 'name' in request.POST:
            enrollment_form = WebinarForm(request.POST)
            if enrollment_form.is_valid():
                enrollment_form.save()
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'error': enrollment_form.errors.as_json()})
    
    # Handle GET requests
    else:
        appointment_form = AppointmentForm()
        enrollment_form = WebinarForm()
        team_members = Team.objects.only('name', 'img', 'post')
    
    return render(request, 'home.html', {
        'form': appointment_form,
        'enrollment_form': enrollment_form,
        'team_members': team_members,  # Pass the team members to the template
    })




def service(request):
    return render(request,"services.html")

def blog(request):
    return render(request,"blog.html")




def teamupdate(request):
    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lpapp:home')  # Redirect to a page listing all team members
    else:
        form = TeamForm()
    return render(request, 'teamupdate.html', {'form': form})




def profile(request, pk):
    team_member = get_object_or_404(Team, pk=pk)
    reviews = Review.objects.filter(team_member=team_member).order_by('-created_at')

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.team_member = team_member
            review.save()

            # Check if the request is AJAX
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({"message": "Review submitted successfully!"}, status=200)

            return redirect('lpapp:profile', pk=pk)
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({"error": "Invalid form submission."}, status=400)

    else:
        form = ReviewForm()

    return render(request, 'profile.html', {
        'team_member': team_member,
        'reviews': reviews,
        'form': form,
    })


def albums(request):
    return render(request,"albums.html")

def contact(request):
    if request.method == 'POST':
        # Retrieve data from the form
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')

        # Save the data into the Appointment model
        try:
            appointment = Appointment.objects.create(
                firstname=firstname,
                lastname=lastname,
                email=email,
                phone_number=phone_number,
                message=message
            )
            return JsonResponse({'success': True, 'message': 'Your appointment has been saved!'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    
    return render(request, "contact.html")

def canada(request):
    if request.method == 'POST':
        # Retrieve data from the form
        candidate = request.POST.get('candidate')
        field = request.POST.get('field')
        phno = request.POST.get('phno')
        exp = request.POST.get('exp')

        # Save the data into the Candidate model
        try:
            immigration = Immigration.objects.create(
                candidate=candidate,
                field=field,
                phno=phno,
                exp=exp,
            )
            return JsonResponse({'success': True, 'message': 'Your assesment has been recorded!'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

    return render(request,"canada.html")

def germany(request):
    return render(request,"germany.html")

def studycanada(request):
    return render(request,"studycanada.html")   
 
def studyeurope(request):
    return render(request,"studyeurope.html")  

def about(request):
    return render(request,"about.html")

def blog1(request):
    return render(request,"blog1.html")

def blog2(request):
    return render(request,"blog2.html")

def blog3(request):
    return render(request,"blog3.html")

def demo(request):
    return render(request,"demo.html")

def careers(request):
    job_listings = Careers.objects.all().order_by('-created_at')  # Fetch jobs sorted by latest
    return render(request, "careers.html", {'job_listings': job_listings})


def hrlp(request):
    return render(request,"hrlp.html")


import os

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from supabase import create_client
from .models import Careers, JobApplication

# Supabase Credentials
SUPABASE_URL = "https://eqqgddahocfmgothdhel.supabase.co"  # Replace with your Supabase URL
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVxcWdkZGFob2NmbWdvdGhkaGVsIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTczNTYxNzA2NywiZXhwIjoyMDUxMTkzMDY3fQ.qXkgqwMOc3hwSmrMwoXG5iZIA8ZF-45ZyRmMGzvgLgY"  # Use your Service Role Key

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def get_signed_url(bucket_name, file_path):
    """Generates a signed URL for private Supabase files."""
    try:
        response = supabase.storage.from_(bucket_name).create_signed_url(file_path, 60*60*24)  # 24-hour expiry
        return response.get("signedURL")
    except Exception as e:
        print(f"Error generating signed URL: {e}")
        return None
    
def upload_to_supabase(file, filename):
    bucket_name = "resume"
    file_path = f"resumes/{filename}"  # Ensure this matches your folder structure

    try:
        file_bytes = file.read()
        
        # ✅ Upload with the correct MIME type
        supabase.storage.from_(bucket_name).upload(
            file_path, 
            file_bytes, 
            {"content-type": "application/pdf"}
        )

        # ✅ Return the direct download link
        return f"{SUPABASE_URL}/storage/v1/object/public/{bucket_name}/{file_path}"

    except Exception as e:
        print(f"Unexpected Error: {e}")
        return None



def jobdetails(request, slug):
    job = get_object_or_404(Careers, slug=slug)

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        resume = request.FILES.get("resume")

        if name and email and resume:
            # ✅ Upload resume to Supabase
            resume_url = upload_to_supabase(resume, resume.name)

            if resume_url:
                JobApplication.objects.create(job=job, name=name, email=email, resume=resume_url)
                messages.success(request, "Application submitted successfully.Please consider a cool off period of 30 days")
            else:
                messages.error(request, "Error uploading your resume. Please try again.")

            return redirect("lpapp:jobdetails", slug=slug)
        else:
            messages.error(request, "Please fill in all fields.")

    return render(request, "jobdetails.html", {"job": job})

def uploadjob(request):
    if request.method == 'POST':
        form = CareersForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Job posting uploaded successfully!")
            return redirect('lpapp:uploadjob')  # Redirect to the same page to avoid form resubmission
        else:
            messages.error(request, "Error uploading job posting. Please check your input.")
    else:
        form = CareersForm()
    
    return render(request, "uploadjob.html", {'form': form})


def job_applications(request):
    
    applications = JobApplication.objects.all().order_by("-applied_at")

    if request.method == "POST":
        for app in applications:
            status_key = f"status_{app.id}"
            new_status = request.POST.get(status_key, app.status)  # Default to existing status if not found
            if new_status != app.status:
                app.status = new_status
                app.save()

        return render(request, "applications.html", {"applications": applications, "message": "Changes saved successfully!"})

    return render(request, "applications.html", {"applications": applications})


def delete_application(request, app_id):
    """Deletes a job application based on the given ID."""
    if request.method == "POST":
        try:
            application = get_object_or_404(JobApplication, id=app_id)
            application.delete()
            return JsonResponse({"success": True})
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})
    
    return JsonResponse({"success": False, "error": "Invalid request"}, status=400)