from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpRequest
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import User
from . forms import StudentForm
from . models import Student
# Create your views here.

def VoteView(request):
    return render(request,'vote.html')
def DashboardView(request):
    return render(request,'dashboard.html')
def CandidatesView(request):
    return render(request,'candidates.html')
def ContactView(request):
    return render(request,'contact.html')
def VotingView(request):
    return render(request,'voting.html')
def RoView(request):
    # Hardcoded credentials
    correct_username = 'RO@C1O3LL4E7GE'
    correct_password = 'SMS74YG'

    if request.method == 'POST':
        # Get the submitted username and password directly from the request
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Print for debugging to check the values
        print(f"Submitted Username: {username}, Submitted Password: {password}")

        # Compare the submitted credentials with the hardcoded values
        if username == correct_username and password == correct_password:
            # Authentication is successful

            # Try to fetch or create a dummy user
            user, created = User.objects.get_or_create(username=username)

            # Log in the user (simulating login)
            login(request, user)  
            return redirect('dashboardview')  # Redirect to the dashboard page
        else:
            # If authentication fails, show an error message
            print("Authentication failed. Invalid username or password.")
            messages.error(request, "Invalid username or password")
    else:
        # Handle GET request (form is shown)
        pass

    return render(request, 'RO.html')  # Render the login page

def student_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')  # Redirect to a success page
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})


def student_list(request):
    students = Student.objects.all()
    print(students) # Fetch all students from the database
    return render(request, 'student_list.html', {'students': students})

from django.shortcuts import render, redirect
from .forms import CandidateForm

def CandidatesRegister(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST, request.FILES)  # Include request.FILES for file handling
        if form.is_valid():
            form.save()
            return redirect('candidatesregister')  # Redirect to the same page or another page after successful submission
    else:
        form = CandidateForm()

    return render(request, 'candidatesregister.html', {'form': form})
