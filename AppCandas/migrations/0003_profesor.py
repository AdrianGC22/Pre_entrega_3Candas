# Generated by Django 5.0.3 on 2024-04-14 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCandas', '0002_alumno'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('DNI', models.IntegerField()),
                ('titulo', models.CharField(max_length=50)),
            ],
        ),
    ]
