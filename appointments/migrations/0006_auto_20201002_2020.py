# Generated by Django 3.1.1 on 2020-10-02 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0005_auto_20201002_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='done',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='notes',
            field=models.TextField(blank=True, default='', max_length=500, null=True),
        ),
    ]
