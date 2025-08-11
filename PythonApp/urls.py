from django.urls import path
from.import views



urlpatterns = [
    path('home/',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('contact/',views.contact_view, name= 'contact'),
    # path('Login/',views.custom_login_view, name='Login'),
    path('regi/',views.Registration_form, name='Registration'),
    # path('regi/',views.register_view, name='Registration'),

    path('login/',views.custom_login_view,name=  'custom_login'),
    path('logout/',views.custom_logout_view,name=  'custom_logout'),
    path('home2/',views.home_views, name='home2'),
    path('course/',views.course_selection, name='course'),
    # path('home2/',views.profile_edit, name=''),
    # path('reset/',views.reset_password, name= 'reset_password'),
    path('password/',views.Password_change, name= 'Password_change'),


    # path('update/',views.profile_edit, name='update'),

]


    