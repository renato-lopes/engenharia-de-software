# Generated by Django 2.2 on 2019-05-31 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_forumuser_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forumuser',
            name='photo',
            field=models.ImageField(default='user.ico', upload_to='images/'),
        ),
    ]