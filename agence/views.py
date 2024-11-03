from django.shortcuts import render
from agence.models import Agence, Property,PropertyImages, Agent, Message, Brand, Blog
from django.core.mail import send_mail
from django.utils import timezone

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView

# def base(request):
#     # agence = Agence.objects.get_or_create()
#     agence = Agence.objects.get(pk=1)
    
#     context = {'agence' : agence, 'page_title' : 'Home'}
#     return render(request, 'base.html',context)

class HomePageView(TemplateView):
    # model = Property
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  
        
        context["agence"] = Agence.objects.get(pk=1)
        context["page_title"] = ''
      
        # context["latest_properties"] = Property.objects.all()[:5]
        context["object_list"] = Property.objects.all()

        context["agents"] = Agent.objects.all()
        context["blogs"] = Blog.objects.filter(is_shown=True)
        return context

class PropertyListView(ListView):
    model = Property
    template_name = 'property-list.html'
    paginate_by = 4
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context["agence"] = Agence.objects.get(pk=1)
        context["page_title"] = 'Properties'

        return context  # {% for property in object_list %}

class PropertyDetailView(DetailView):
    model = Property
    template_name = 'property-detail.html'
    
    # def get_context_data(self, **Kwargs):
    #     context = super().get_context_data(**Kwargs)
    #     return context
   

class BlogListView(ListView):
    model = Blog
    template_name = 'blog.html'
    paginate_by = 4
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)   
        context["agence"] = Agence.objects.get(pk=1)
        context["page_title"] = 'Blog'
        context["properties"] = Property.objects.all()
        context["blogs"] = Blog.objects.filter(is_shown=True)
        return context  # {% for property in object_list %}



# def index(request):
#     agence = Agence.objects.get_or_create()
#     agence = Agence.objects.get(id=1)
#     properties = Property.objects.all()
#     agents = Agent.objects.all()
#     brands = Brand.objects.all()

#     context = {'agence' : agence,  'page_title' : '', 'properties' : properties,
#                'agents' : agents, 'brands' : brands}
#     return render(request, 'index.html',context)


def sendmessage(request):
    if request.method == 'POST':
        author = request.POST['author']
        email = request.POST['email']
        subject = request.POST['subject']
        comment = request.POST['comment']
        
        message = Message.objects.create(
            author = author,
            email = email,
            subject = subject,
            comment = comment,                  
        )     
        
        # send an email
        send_mail (
            author + ' ( ' + subject + ' )', # subject
            comment, # message
            email, # from email
            ['bmhwin@gmail.com'], # To email
            fail_silently=False
        )
        
        context = {'author': author}
        return render(request,'contact.html', context)
    else:
        context = {}
        return render(request,'contact.html', context )

       
def gallery(request):
    agence = Agence.objects.get_or_create()
    agence = Agence.objects.get(id=1)
    properties = Property.objects.all()

    context = {'agence': agence,  'page_title':'Gallery', 'properties' : properties}
    return render(request, 'gallery.html',context)


# def property_list(request):
#     agence = Agence.objects.get_or_create()
#     agence = Agence.objects.get(id=1)
#     properties = Property.objects.all()

#     context = {'agence':agence, 'page_title':'Properties', 'properties' : properties}
#     return render(request, 'properties.html',context)
    
# def property_detail(request, slug):
#     agence = Agence.objects.get_or_create()
#     agence = Agence.objects.get(id=1)
#     properties = Property.objects.all()
#     property = Property.objects.get(slug=slug)
#     context = {'agence': agence,  'page_title':'Properties Details',
#                'properties' : properties, 'property':property}
#     return render(request, 'properties-detail.html',context)


def agent_detail(self,slug):
    pass

def contact(request):
    agence = Agence.objects.get_or_create()
    agence = Agence.objects.get(id=1)
    context={'agence': agence}
    
    return render(request, 'contact.html',context)

# def blog(request):
    
#     agence = Agence.objects.get_or_create()
#     agence = Agence.objects.get(id=1)
#     properties = Property.objects.all()

#     context = {'agence': agence,  'page_title':'Blog',  'properties' : properties}
#     return render(request, 'blog.html',context)

def register(request):
    context={}
    return render(request, 'register.html',context)

def signin(request):
    context={}
    return render(request, 'signin.html',context)
