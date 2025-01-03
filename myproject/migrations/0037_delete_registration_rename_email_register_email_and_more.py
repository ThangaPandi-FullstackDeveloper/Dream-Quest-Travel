# Generated by Django 5.1.3 on 2024-11-25 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0036_register'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Registration',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='email',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='first_name',
            new_name='User_Name',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='last_name',
            new_name='full_Name',
        ),
        migrations.RemoveField(
            model_name='register',
            name='phone',
        ),
        migrations.AddField(
            model_name='register',
            name='Confirm_Password',
            field=models.CharField(default='default_password', max_length=128),
        ),
        migrations.AddField(
            model_name='register',
            name='Password',
            field=models.CharField(default='default_password', max_length=128),
        ),
        migrations.AddField(
            model_name='register',
            name='Phone_Number',
            field=models.IntegerField(default='default_password', max_length=128),
        ),
    ]
