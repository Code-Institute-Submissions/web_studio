# Generated by Django 3.1.1 on 2020-10-02 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelancers', '0004_freelancer_phone_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freelancer',
            name='on_the_job',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
