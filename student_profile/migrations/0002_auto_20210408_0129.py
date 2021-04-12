# Generated by Django 3.1.7 on 2021-04-07 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='students',
            name='student_department',
            field=models.CharField(default='uncategorized', max_length=30),
        ),
    ]