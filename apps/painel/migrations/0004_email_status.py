# Generated by Django 4.1.3 on 2022-11-20 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('painel', '0003_email_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='status',
            field=models.CharField(choices=[('L', 'Lido'), ('N', 'Não lido')], default=1, max_length=10),
            preserve_default=False,
        ),
    ]
