# Generated by Django 4.0.3 on 2022-03-21 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('imgPath', models.ImageField(upload_to='photos/movie')),
                ('duration', models.IntegerField()),
                ('genre', models.CharField(max_length=200)),
                ('language', models.CharField(max_length=200)),
                ('mpaaRating_type', models.CharField(max_length=200)),
                ('mpaaRating_label', models.CharField(max_length=200)),
                ('userRating', models.IntegerField()),
            ],
        ),
    ]
