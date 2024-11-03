from django.urls import path
from agence import views
from agence.views import HomePageView , PropertyListView , PropertyDetailView, BlogListView

app_name = 'agence'

urlpatterns = [
    # path('',views.index, name="index"),
    # path('property-list',views.property_list, name="property-list"),
    # path('<slug:slug>/',views.property_detail, name="property-detail"),
    # path('',views.base, name="base"),
    
    path('', HomePageView.as_view(), name="home"),
    path('properties',PropertyListView.as_view(), name="property-list"),
    path('<slug:slug>/',PropertyDetailView.as_view(), name="property-detail"),
   path('blog',BlogListView.as_view(), name="blog"),
   
    path('gallery',views.gallery, name="gallery"),
    path('<slug:slug>/',views.agent_detail, name="agent-detail"),
    path('contact',views.contact, name="contact"),
    path('sendmessage',views.sendmessage, name="sendmessage"),
    # path('blog',views.blog, name="blog"),
    path('register',views.register, name="register"),
    path('signin',views.signin, name="signin"),
    

]