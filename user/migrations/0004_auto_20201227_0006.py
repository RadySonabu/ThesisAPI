# Generated by Django 3.1.1 on 2020-12-26 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20200928_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='role',
            field=models.CharField(choices=[(1, 'patient'), (2, 'doctor'), (3, 'developer')], max_length=60),
        ),
        migrations.DeleteModel(
            name='Role',
        ),
    ]
