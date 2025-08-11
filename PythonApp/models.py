from django.db import models

# For CONTACT

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"


# Registration Form

class Student(models.Model):
    GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]
    COURSE_CHOICES = [
    ('Data Science', 'Data Science & AI Course'),
    ('Data Analytics', 'Data Analytics Course'),
    ('Microsoft', 'Microsoft Power BI Course'),   
    ('python', 'Python Full Stack'),
    ('java', 'Java Full Stack'),
    ('PHP', 'PHP Full Stack'), 
    ]

    first_name= models.CharField(max_length=50 ,default='na')
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=100, default=1234)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    dob = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    country = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    hobbies = models.CharField(max_length=200)
    avatar = models.FileField(upload_to='documents/' ,default='none')
    course = models.CharField(max_length=50, choices=COURSE_CHOICES,default='python',null=True, blank=True)
    is_email_verified = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.first_name } {self.last_name }"


#--REGISTRATION FORM--

# class Student(models.Model):
#     first_name=models.CharField(max_length=50)
#     last_name=models.CharField(max_length=100)
#     GENDER_CHOICES = [('male', "Male"), ('female', "Female"),('other', "Other")]
#     user_gender = models.CharField(max_length=100, choices=GENDER_CHOICES)
#     dob=models.DateField()
#     email=models.EmailField(max_length=200)
#     country=models.CharField(max_length=100)
#     state=models.CharField(max_length=100)
#     city=models.CharField(max_length=100)
#     hobbies=models.CharField(max_length=300)
#     avatar=models.FileField(upload_to='documents/',default='none')

#     def __str__(self):
#         return self.first_name

#test example

class Boyz(models.Model):
    name= models.CharField(max_length=100)
    age= models.IntegerField(default=0)
    email=models.EmailField(default='none')