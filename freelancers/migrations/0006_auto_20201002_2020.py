# Generated by Django 3.1.1 on 2020-10-02 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelancers', '0005_auto_20201002_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freelancer',
            name='current_project',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='freelancer',
            name='on_the_job',
            field=models.BooleanField(default=False),
        ),
    ]
