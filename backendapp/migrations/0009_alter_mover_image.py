# Generated by Django 4.0.4 on 2022-05-11 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendapp', '0008_alter_mover_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mover',
            name='image',
            field=models.CharField(max_length=10000, null=True),
        ),
    ]