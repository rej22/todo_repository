# Generated by Django 4.1.4 on 2023-03-08 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp01', '0003_task_taskdescription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='taskDescription',
            field=models.TextField(),
        ),
    ]
