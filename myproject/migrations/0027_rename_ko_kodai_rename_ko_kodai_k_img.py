# Generated by Django 5.1.3 on 2024-11-23 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0026_rename_kodai_ko_rename_kodai_ko_ko'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ko',
            new_name='Kodai',
        ),
        migrations.RenameField(
            model_name='kodai',
            old_name='ko',
            new_name='k_img',
        ),
    ]