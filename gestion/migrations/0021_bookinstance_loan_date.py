# Generated by Django 2.2.5 on 2020-03-23 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0020_auto_20200319_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinstance',
            name='loan_date',
            field=models.DateField(auto_now=True),
        ),
    ]
