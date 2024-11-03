from django.contrib import admin
from .models import * # Agence, Brand, Type, Property, PropertyImages, Agent, Message, Blog, Client, Service

class AgenceAdmin(admin.ModelAdmin):
    list_display = ['name', 'logo', 'agencelogo', 'address','id']    

class BrandAdmin(admin.ModelAdmin):
    ordering = ('-start',)
    list_display = ['name','image', 'brand_image', 'start', 'end','is_active']   
     
class TypeAdmin(admin.ModelAdmin):
    ordering = ('name',)
    list_display = ['name', 'image', 'type_image', 'is_active']    

class PropertyImagesAdmin(admin.TabularInline):
    model = PropertyImages
    
class PropertyAdmin(admin.ModelAdmin):
    # search_fields = ('title','type','price',)
    list_filter = ('title','type','price','is_active',)
    ordering = ('-created','title',)
    inlines = [PropertyImagesAdmin]
    list_display = ['type', 'title', 'old_price', 'price','image', 'property_image',
                    'is_active', 'is_new', 'is_featured', 'is_slider']    
    fieldsets = (
        (None,{'fields':('type','title','image','status','address','description')}),
        ('Price',{'fields':('old_price','price')}),
        ('Parameters',{'fields':('rooms','beds','baths','squart','is_active', 'is_new', 'is_featured', 'is_slider',)}),
    )
    
class AgentAdmin(admin.ModelAdmin):
    list_display = ['agent_image', 'name', 'profession', 'mobile', 'email']
    
class MessageAdmin(admin.ModelAdmin):
    list_display = ['author', 'email', 'subject', 'comment','created']    

class BlogAdmin(admin.ModelAdmin):
    list_display = ['author', 'subject', 'comment','blog_image', 'created' , 'is_shown']

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'comment', 'created']
  
class ClientAdmin(admin.ModelAdmin):
    list_display = ['client_image', 'name', 'profession']
  
admin.site.register(Client,ClientAdmin)
admin.site.register(Service,ServiceAdmin)
admin.site.register(Blog,BlogAdmin)
admin.site.register(Agent,AgentAdmin)
admin.site.register(Agence,AgenceAdmin)
admin.site.register(Type,TypeAdmin)
admin.site.register(Property,PropertyAdmin)

admin.site.register(Brand,BrandAdmin)
admin.site.register(Message,MessageAdmin)
