# Generated by Django 4.0.4 on 2022-05-11 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backendapp', '0004_alter_request_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='id_mover',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='request',
            name='id_user',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='mover',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backendapp.mover'),
        ),
        migrations.AlterField(
            model_name='request',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backendapp.reguser'),
        ),
    ]
