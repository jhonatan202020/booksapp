# Generated by Django 2.2.5 on 2020-03-17 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0012_auto_20200317_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='due_back',
            field=models.DateField(blank=True, help_text='Si tiene fecha de devolucion el estado no puede ser Disponible', null=True, verbose_name='Fecha devolución'),
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='status',
            field=models.CharField(blank=True, choices=[('o', 'En prestamo'), ('a', 'Disponible'), ('r', 'Reservado')], default='a', help_text='No puede estar diponible y con fecha de devolucion', max_length=1, verbose_name='Estado'),
        ),
    ]
