# Generated by Django 2.2.5 on 2020-03-17 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0010_auto_20200312_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='gestion', verbose_name='Prestatario'),
        ),
    ]