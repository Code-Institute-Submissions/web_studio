# Generated by Django 3.1.1 on 2020-10-02 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0004_auto_20201001_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='done',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
