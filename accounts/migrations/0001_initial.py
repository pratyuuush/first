# Generated by Django 3.0.5 on 2020-05-18 08:10

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_countries.fields
import imagekit.models.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=100)),
                ('posted_on', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, default='default.jpg', null=True, upload_to='profile_pics')),
                ('bio', models.CharField(default=' ', max_length=200, null=True)),
                ('email', models.EmailField(max_length=70)),
                ('ac_type', models.CharField(choices=[('Individual', 'Individual'), ('Organization', 'Organization')], default=' ', max_length=12)),
                ('address1', models.CharField(default=' ', max_length=1024, verbose_name='Address line 1')),
                ('address2', models.CharField(default=' ', max_length=1024, verbose_name='Address line 2')),
                ('zip_code', models.CharField(default=' ', max_length=10, verbose_name='ZIP / Postal code')),
                ('city', models.CharField(default=' ', max_length=1024)),
                ('state', models.CharField(default=' ', max_length=1024)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=600, null=True)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('rate_type', models.CharField(choices=[('5 Star', '5 Star'), ('4 Star', '4 Star'), ('3 Star', '3 Star'), ('2 Star', '2 Star'), ('1 Star', '1 Star')], default=' ', max_length=7)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_rated', to='accounts.UserProfile')),
                ('reciever', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_recieved', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_something', models.TextField(max_length=1000, null=True)),
                ('posted_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('post_type', models.CharField(choices=[('Job Post', 'Job'), ('Blog Post', 'Blog')], default=' ', max_length=9)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followed', models.BooleanField(default=False, null=True)),
                ('date_posted', models.DateTimeField(blank=True, null=True)),
                ('comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Comment')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Post')),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.UserProfile')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('follow_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow_user', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='post_connected',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user_connected',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
