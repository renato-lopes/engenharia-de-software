# Generated by Django 2.2 on 2019-06-02 01:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.ForumUser'),
        ),
        migrations.AddField(
            model_name='answer',
            name='downvote',
            field=models.ManyToManyField(blank=True, related_name='a_downvote', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='upvote',
            field=models.ManyToManyField(blank=True, related_name='a_upvote', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.ForumUser'),
        ),
    ]
