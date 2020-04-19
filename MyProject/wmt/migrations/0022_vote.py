# Generated by Django 3.0.5 on 2020-04-18 14:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20200416_1337'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wmt', '0021_auto_20200416_1328'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='wmt.Event')),
                ('movie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vote_movie', to='movies.Movie')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vote_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]