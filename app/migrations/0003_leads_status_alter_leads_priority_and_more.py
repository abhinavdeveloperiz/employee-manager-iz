# Generated by Django 5.2.1 on 2025-05-28 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_name_employee_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='leads',
            name='status',
            field=models.CharField(choices=[('Not Accepted', 'Not Accepted'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], default='Not Accepted', max_length=50),
        ),
        migrations.AlterField(
            model_name='leads',
            name='Priority',
            field=models.CharField(choices=[('Hot', 'Hot'), ('Warm', 'Warm'), ('Cold', 'Cold')], default='Hot', max_length=50),
        ),
        migrations.AlterField(
            model_name='leads',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
