# Generated by Django 2.2.5 on 2020-03-12 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0007_auto_20200312_1123'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back']},
        ),
    ]
