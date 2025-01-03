# Generated by Django 5.1.3 on 2024-11-26 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0051_rename_registrationform_registration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book_now',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('City_of_Residence', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Phone_Number', models.BigIntegerField(blank=True, default=None, null=True)),
                ('Whats_Number', models.BigIntegerField(blank=True, default=None, null=True)),
                ('Travel_Destination', models.CharField(max_length=100)),
                ('Date_of_Travel', models.DateField()),
                ('No_of_People', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Registration',
        ),
    ]
