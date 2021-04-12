# Generated by Django 3.1.7 on 2021-04-12 07:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mail_system', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mailbox',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='mailbox',
            name='mail_save_Date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]