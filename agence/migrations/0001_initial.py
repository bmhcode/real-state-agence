# Generated by Django 4.1.7 on 2024-10-26 14:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='Agence name', max_length=255, verbose_name='Agence name')),
                ('address', models.CharField(blank=True, default='Agence address', max_length=255, null=True)),
                ('phone', models.CharField(blank=True, default='Agence phone', max_length=255, null=True, verbose_name='Contact Phone')),
                ('email', models.EmailField(default='agencemail@gmail.com', max_length=255, verbose_name='Email Address')),
                ('logo', models.ImageField(blank=True, default='logo.jpg', upload_to='agence', verbose_name='logo')),
                ('image', models.ImageField(blank=True, default='agence image', upload_to='agence')),
                ('about_us', models.TextField(blank=True, default='About Us', null=True)),
            ],
            options={
                'verbose_name_plural': 'Agences',
            },
        ),
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40, null=True, verbose_name='name')),
                ('profession', models.CharField(blank=True, max_length=60, null=True, verbose_name='profession')),
                ('image', models.ImageField(default='agent.jpg', upload_to='agent')),
                ('email', models.EmailField(blank=True, default='', help_text='agentmail@gmail.com', max_length=255, null=True, verbose_name='Email address')),
                ('mobile', models.CharField(max_length=20, verbose_name='mobile')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated at')),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(blank=True, max_length=64, null=True, verbose_name='author')),
                ('subject', models.CharField(blank=True, max_length=64, null=True, verbose_name='subject')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='content')),
                ('image', models.ImageField(default='blog.jpg', upload_to='blog')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('is_shown', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Brand name', max_length=255, verbose_name='Brand name')),
                ('image', models.ImageField(blank=True, default='brand.jpg', upload_to='brand-images', verbose_name='Brand')),
                ('start', models.DateField(verbose_name='Start at')),
                ('end', models.DateField(verbose_name='End at')),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-start'],
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40, null=True, verbose_name='name')),
                ('profession', models.CharField(blank=True, max_length=60, null=True, verbose_name='profession')),
                ('image', models.ImageField(default='client.jpg', upload_to='client')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='content')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('is_shown', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(blank=True, max_length=64, null=True, verbose_name='author')),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(blank=True, max_length=64, null=True, verbose_name='subject')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='content')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('For Sale', 'For Sale'), ('For Rent', 'For Rent'), ('Sold Out', 'Sold Out')], default='', help_text='For Sale, For Rent,', max_length=30)),
                ('title', models.CharField(max_length=128, verbose_name='title of property')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('address', models.CharField(blank=True, default='Property adress', max_length=255, null=True)),
                ('description', models.TextField(blank=True, default='This property is ...', help_text='infos about ', null=True, verbose_name='informations about product')),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('old_price', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True, verbose_name='old price')),
                ('image', models.ImageField(default='property.jpg', upload_to='property')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('is_active', models.BooleanField(default=False)),
                ('is_new', models.BooleanField(default=False)),
                ('is_featured', models.BooleanField(default=False)),
                ('is_slider', models.BooleanField(default=False)),
                ('rooms', models.IntegerField(verbose_name='rooms')),
                ('beds', models.IntegerField(verbose_name='beds')),
                ('baths', models.IntegerField(verbose_name='baths')),
                ('squart', models.IntegerField(verbose_name='squart')),
            ],
            options={
                'verbose_name': 'Property',
                'verbose_name_plural': 'Properties',
                'ordering': ['-updated', '-created'],
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64, null=True, verbose_name='service')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='content')),
                ('image', models.ImageField(default='service.jpg', upload_to='service')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('is_shown', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Type')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('image', models.ImageField(default='type.jpg', upload_to='type-images')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'types',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='PropertyImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='property.jpg', upload_to='property-images')),
                ('description', models.CharField(blank=True, max_length=64, null=True, verbose_name='Description')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('property', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='images', to='agence.property', verbose_name='Property')),
            ],
            options={
                'verbose_name_plural': 'Property Images',
            },
        ),
        migrations.AddField(
            model_name='property',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='type', to='agence.type'),
        ),
        migrations.AddField(
            model_name='property',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]