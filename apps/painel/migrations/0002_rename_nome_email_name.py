# Generated by Django 4.1.3 on 2022-11-20 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('painel', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='email',
            old_name='nome',
            new_name='name',
        ),
    ]
