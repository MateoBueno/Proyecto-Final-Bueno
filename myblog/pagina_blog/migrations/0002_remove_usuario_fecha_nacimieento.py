# Generated by Django 4.1.5 on 2023-01-24 02:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pagina_blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='fecha_nacimieento',
        ),
    ]
