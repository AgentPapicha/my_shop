# Generated by Django 4.2.6 on 2023-11-18 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('article_text', models.TextField()),
                ('slug', models.SlugField()),
                ('author_name', models.CharField(max_length=100)),
                ('created_at', models.DateField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/blog_images/')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='uploads/blog_thumbnails/')),
            ],
        ),
    ]
