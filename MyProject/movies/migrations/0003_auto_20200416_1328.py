# Generated by Django 3.0.3 on 2020-04-16 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_movie_review_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movie_published',
            field=models.CharField(max_length=10),
        ),
    ]