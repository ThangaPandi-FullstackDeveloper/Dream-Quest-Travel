# Generated by Django 5.1.3 on 2024-11-18 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0003_rename_img_g_winder_im'),
    ]

    operations = [
        migrations.CreateModel(
            name='G_summer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i', models.ImageField(upload_to='pic')),
                ('plan', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=100)),
            ],
        ),
    ]