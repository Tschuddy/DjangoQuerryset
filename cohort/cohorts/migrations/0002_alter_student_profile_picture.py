# Generated by Django 5.0 on 2024-11-05 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cohorts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='profile_picture',
            field=models.URLField(verbose_name='Profile Image URL'),
        ),
    ]
