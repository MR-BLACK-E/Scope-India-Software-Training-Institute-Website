from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.http import HttpResponse
# from django.core.mail import EmailMessage
from django.views import *
# from rest_framework import generics

from django.contrib import messages

from .forms import StudentRegistrationForm
from .models import Student
from django.core.mail import send_mail

# from django.conf import settings
# from django.urls import reverse
# from django.utils.crypto import get_random_string

# DATAS FROM USER
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout 

# MY VIEWS

def home(request): 
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

# def contact(request):
#     return render(request,'Contact.html') 

# def Login(request):
#     return render(request,'Login.html')

# def Registration(request):
#     return render(request,'Registration.html')



#-- contact email--

#Mail save to database
def message_file(request):
    if request.method== 'POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'Contact.html',{'form':form, 'success':True})
    else:
        form= ContactForm()
    return render(request, 'Contact.html', {'form': form})       

#Mail sending
def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('from')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact=Contact(
            name= name,
            email= email,
            subject= subject,
            message= message
        )
        contact.save()

        try:
            send_mail(
                subject,
                f"Thank You {name}. Your message:{message}, received successfully. We will contact you soon!",
                 'emilmathew@gmail.com',
                 [email],
            )
        
            
            messages.success(request, "Your message was sent successfully!") 
        except Exception as e:
            messages.error(request, "Failed to send your message. Please try again.")

        return redirect('contact') 
    return render(request, 'contact.html')



#email verification
email_verification_tokens = {}  


def verify_email(request, token):
    email = email_verification_tokens.get(token)
    if email:
        try:
            student = Student.objects.get(email=email)
            student.is_email_verified = True
            student.save()
            messages.success(request, 'Email verified successfully!')
        except Student.DoesNotExist:
            messages.error(request, 'Invalid verification link.')
    else:
        messages.error(request, 'Invalid or expired token.')
    return redirect('Registration')

#Registration Form
def Registration_form(request):
     if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        country = request.POST.get('country')
        state = request.POST.get('state')
        city = request.POST.get('city')
        hobbies = request.POST.get('hobbies')
        avatar = request.POST.get('avatar')
        course = request.POST.get('course')
        # is_email_verified = is_email_verified('is_email_verified')

        student = Student(
            first_name = first_name,
            last_name=last_name,
            password=password,
            gender=gender,
            dob=dob,
            email=email,
            phone=phone,
            country=country,
            state=state,
            city=city,
            hobbies= hobbies,
            avatar= avatar,
            course=course,
            # is_email_verified = is_email_verified
        )
        
    #     student.save()
        form = StudentRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save(commit=False)
            student.is_email_verified = False
            student.save()
            if request.method == 'POST':
                username=request.POST['email']
                password=request.POST['password'] 
                User.objects.create(username=username, password=make_password(password))       
            #     return redirect('custom_login')
            # return render(request,'Registration.html')

            messages.success(request, 'Registration successful!')
            return redirect('Registration')
        else:
            messages.error(request,"Registration failed. Email already exist")
            return redirect('Registration')
     else:
        form = StudentRegistrationForm()
     return render(request, 'Registration.html', {'form': form })

#Password create
def register_view(request):

    if request.method == 'POST':
        username=request.POST['email']
        password=request.POST['password'] 
        User.objects.create(username=username, password=make_password(password))       
        return redirect('custom_login')
    return render(request,'Registration.html')

# --COURSE SELECTION--  

def course_selection(request):
    if request.method == 'POST':
        course = request.POST.get('course')
        student= Student(
            course = course
        )
        form = Course(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            messages.success(request, 'Course Registration successful!')
            return redirect('course')
        else:
            messages.error(request,"Course Registration failed.")
            return redirect('course')
    form = Course()
    return render(request, 'Course_selection.html', {'form': form })  
   
# --PROFILE VIEW--     
def profile_view(request):
    student=Student.objects.get(user=student)
    return render(request, 'Login_home.html', {'student': student})


#--LOGIN PAGE--
def custom_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')

        user = authenticate(request, username= username , password= password)

        if user is not None:
            login(request,user)
            response = redirect('home2')

            if remember_me:
                response.set_cookie('logged_in_user', username, max_age=60*60*24*30) 
            else:
                response.set_cookie('logged_in_user', username, max_age=60*60) 

            return response
        else:
            messages.error(request,"invalid email or password")
            return redirect('custom_login')
    return render (request, 'Login.html')

def custom_logout_view(request):
    logout(request)
    response = redirect('custom_login')
    response.delete_cookie('logged_in_user') 
    return response

# PROFILE VIEW
def home_views(request):
    
    if request.user.is_authenticated:
        student=Student.objects.get(email=request.user)

        user = request.user

        if request.method == 'POST':
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            # user.password = request.POST.get('password')
            user.gender = request.POST.get('gender')
            user.dob = request.POST.get('dob')
            # user.email = request.POST.get('email')
            user.phone = request.POST.get('phone')
            user.country = request.POST.get('country')
            user.state = request.POST.get('state')
            user.city = request.POST.get('city')
            user.hobbies = request.POST.get('hobbies')
            user.avatar = request.POST.get('avatar')
            user.course = request.POST.get('course')
            # User.objects.create( password=make_password(user.password))
          
            form = StudentEditForm(request.POST, request.FILES,instance=student)
            if form.is_valid():
                student = form.save(commit=False)
                student.save()
                  
                messages.success(request, 'Profile updated!')
                return redirect('home2')
            else:
                messages.error(request,"Profile update failed!")
                return redirect('home2')
        else:
            form = StudentEditForm()
        # return render(request, 'Login_home.html', {'form': form})

        return render(request, 'Login_home.html', {'username':request.user.username, 'student':student, 'form': form})
    else:
        return redirect('home2')   


# password edit
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Student

# def Password_change(request):
#     if not request.user.is_authenticated:
#         return redirect('home2')  # Redirect if not logged in

#     if request.method == 'POST':
#         email = request.POST.get('email')
#         new_password = request.POST.get('password')

#         try:
#             # Fetch the student by email
#             user = Student.objects.get(email=email)
            
#             # Ensure the logged-in user matches the email
#             if user.email == request.user.email:
#                 user.password = make_password(new_password)
#                 user.save()
#                 messages.success(request, "Password has been reset. You can log in with your new password.")
#                 return redirect('custom_login')
#             else:
#                 messages.error(request, "Invalid email for the logged-in user.")
#         except Student.DoesNotExist:
#             messages.error(request, "No account found with this email.")

#     return render(request, 'Password_change.html')

def Password_change(request):
    if not request.user.is_authenticated:
        return redirect('home2')

    if request.method == 'POST':
        new_password = request.POST.get('password')
        request.user.password = make_password(new_password)
        request.user.save()
        messages.success(request, "Password updated successfully.")
        return redirect('custom_login')

    return render(request, 'Password_change.html')


# def reset_password(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         try:
#             user = Student.objects.get(email=email)
#             if user.email == email:
#                 user.password = make_password(password)
#                 user.save()
#                 messages.success(request,"Password has been reset. You can Login with your new password")
#                 return redirect('custom_login')
#             else:
#                 messages.error( request,"error: Invalid email.")
#         except Student.DoesNotExist:
#             return redirect('home2')
#     return render(request,'Password_change.html')
    
    # else:
    #     return redirect('home2')   

# from django.contrib.auth import update_session_auth_hash
#             update_session_auth_hash(request, user)

# def Password_change(request):
#     if request.user.is_authenticated:
       
#         if request.method == 'POST':
#             user = Student.objects.get(email=request.user) 
#             user= request.user
#             email = request.POST.get('email')
#             new_password = request.POST.get('password')
        
#             try:
#                 user = Student.objects.get(email=request.user) 
#                 if user.email == email:
#                     user.password= make_password(new_password)
#                     user.save()
#                     messages.success(request,"Password has been reset. You can Login with your new password")
#                     return redirect('custom_login')
#                 else:
#                     messages.error( request,"error: Invalid email.")
#             except Student.DoesNotExist:
#                 return redirect('home2')
#     return render(request,'Password_change.html')


# def Password_change(request):
#     if request.user.is_authenticated:
#         student=Student.objects.get(email=request.user)

#         user = request.user
#         if request.method == 'POST':

#             # user.email=request.POST.get('email')
#             user.password=request.POST.get('password') 
#             User.objects.create( password=make_password(user.password))   

#             form = Password(request.POST,instance=student)
#             if form.is_valid():
#                 student = form.save(commit=False)
#                 student.save()

#             return redirect('custom_login')
#     return render(request,'Password_change.html')


# PROFILE EDIT

# def profile_edit(request):
#     student = request.user

#     if request.method == 'POST':
#         student.first_name = request.POST.get('first_name1')
#         student.last_name = request.POST.get('last_name1')
#         student.password = request.POST.get('password1')
#         student.gender = request.POST.get('gender1')
#         student.dob = request.POST.get('dob1')
#         student.email = request.POST.get('email1')
#         student.phone = request.POST.get('phone1')
#         student.country = request.POST.get('country1')
#         student.state = request.POST.get('state1')
#         student.city = request.POST.get('city1')
#         student.hobbies = request.POST.get('hobbies1')
#         student.avatar = request.POST.get('avatar1')

#         student = Student(
#             first_name = student.first_name,
#             last_name=student.last_name,
#             password=student.password,
#             gender=student.gender,
#             dob=student.dob,
#             email=student.email,
#             phone=student.phone,
#             country=student.country,
#             state=student.state,
#             city=student.city,
#             hobbies= student.hobbies,
#             avatar= student.avatar,
#             # is_email_verified = is_email_verified
#         )
#         # student.save()
#     #     student.save()
#     #     messages.success(request, "Profile updated!")
#     #     return redirect('home2')

#     # return render(request, 'Login_home.html', {'student': request.student})
#         form = StudentEditForm(request.POST, request.FILES)
#         if form.is_valid():
#             student = form.save(commit=False)
#             student.is_email_verified = False
#             student.save()
#             if request.method == 'POST':
#                 username=request.POST['email1']
#                 password=request.POST['password1'] 
#                 User.objects.create(username=username, password=make_password(password))       

#             messages.success(request, 'Profile updated!')
#             return redirect('update')
#         else:
#             messages.error(request,"Profile update failed!")
#             return redirect('update')
#     else:
#         form = StudentEditForm()
#     return render(request, 'Update_profile.html', {'form': form})

# --Add Subject--

# def Profile_update(request):
    

    #     messages.success(request, "Profile updated!")
    #     return redirect('home2')

    # return render(request, 'Login_home.html', {'student': student})

        # student.save()
    #     form = StudentRegistrationForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         student = form.save(commit=False)
    #         # messages.success(request, 'Registration successful!')
    #         # return redirect('Registration')

    #         student.is_email_verified = False
    #         student.save()
    #         messages.success(request, 'Registration successful!')
    #         return redirect('Registration')
    #     else:
    #         messages.error(request,"Registration failed. ")
    #         return redirect('Registration')
    #  else:
    #     form = StudentRegistrationForm()
    #  return render(request, 'Registration.html', {'form': form})

    #     if email:
    #         try:
    #             student = Student.objects.get(email=email)
    #             # student.is_email_verified = True
    #             student.save()
    #             messages.success(request, 'Email verified successfully!')
    #         except Student.DoesNotExist:
    #             messages.error(request, 'Invalid verification link.')
    #     else:
    #         messages.error(request, 'Invalid or expired token.')
    #     return redirect('Registration')
    #  else:
    #     form = StudentRegistrationForm()
    #  return render(request, 'Registration.html', {'form': form})



# Assume you have a separate model or method to generate and store email tokens
email_verification_tokens = {}  # temp in-memory store

# def Registration(request):
#     if request.method == 'POST':
#         form = StudentRegistrationForm(request.POST, request.FILES)
#         if form.is_valid():
#             student = form.save(commit=False)
#             student.is_email_verified = False
#             student.save()
            
#             # Send email confirmation
#             token = get_random_string(32)
#             email_verification_tokens[token] = student.email
#             verification_url = request.build_absolute_uri(reverse('verify_email', args=[token]))
#             send_mail(
#                 subject='Verify your registration',
#                 message=f"Click the link to verify your email: {verification_url}",
#                 from_email=settings.DEFAULT_FROM_EMAIL,
#                 recipient_list=[student.email],
#             )
#             messages.success(request, 'Registration successful! Please check your email to confirm.')
#             return redirect('Registration')
#         else:
#             messages.error(request, 'Registration failed. Please check the form.')
#     else:
#         form = StudentRegistrationForm()
#     return render(request, 'Registration.html', {'form': form})

#  LOGIN PAGE 2   
# from django.contrib.auth.models import User
# from django.contrib.auth.hashers import make_password
# from django.contrib.auth import authenticate, login, logout


# def custom_login_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         remember_me = request.POST.get('remember_me')

#         user = authenticate(request, username=username , password=password)

#         if user is not None:
#             login(request,user)
#             response = redirect('home2')

#             if remember_me:
#                 response.set_cookie('logged_in_user', username, max_age=60*60*24*30) #30 days
#             else:
#                 response.set_cookie('logged_in_user', username, max_age=60*60) #1 hour

#             return response
#         else:
#             return HttpResponse("invalid username or password")
#     return render (request, 'Login.html')

# def custom_logout_view(request):
#     logout(request)
#     response = redirect('custom_login')
#     response.delete_cookie('logged_in_user') 
#     return response

# def home_views(request):
#     if request.user.is_authenticated:
#         return render(request, 'Login_home.html', {'username':request.user.username})
#     else:
#         return redirect('custom_login')   

# def register_view(request):
#     if request.method == 'POST':
#         username=request.POST['username']
#         password=request.POST['password'] 
#         User.objects.create(username=username, password=make_password(password))       
#         return redirect('custom_login')
#     return render(request,'Registration.html')
 

 #  --Contact Form --


# views.py by buddy
# from django.shortcuts import render, redirect
# from django.core.mail import send_mail
# from django.contrib import messages
# from .forms import ContactForm
# from django.conf import settings

# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             contact = form.save()

#             # Send email to info@scopeindia.org
#             try:
#                 send_mail(
#                     subject=f"[Contact] {contact.subject}",
#                     message=f"From: {contact.name} <{contact.email}>\n\n{contact.message}",
#                     from_email=settings.DEFAULT_FROM_EMAIL,
#                     recipient_list=['emilmathew1311@gmail.com'],
#                 )
#                 messages.success(request, "Your message was sent successfully.")
#             except Exception as e:
#                 messages.error(request, "Unable to send your message right now. Please try again later.")
#             return redirect('contact')
#         else:
#             messages.error(request, "Please fix the errors below.")
#     else:
#         form = ContactForm()
#     return render(request, 'Contact.html', {'form': form})


# Contact Form

# def contact(request):
#     if request.method =='POST':
#         name=request.POST.get("name")
#         # to_email = request.POST.get("to_email")
#         from_email = [request.POST.get("from")]
#         subject = request.POST.get("subject")
#         message = request.POST.get("message")
#         # file_upload = request.FILES.get("attachment")

#         mail=EmailMessage(name,subject,message,from_email)

#         # if message:
#         #     mail.attach()

#         try:
#             mail.send()
#             messages.success(request,"email send successfully")
#         except Exception as e:
#             return HttpResponse(f"Failed to send email:{str(e)}")

#     return render(request,'Contact.html')
    
