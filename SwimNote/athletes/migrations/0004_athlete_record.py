# Generated by Django 4.0.5 on 2022-07-01 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('athletes', '0003_personalbest'),
    ]

    operations = [
        migrations.AddField(
            model_name='athlete',
            name='record',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='athletes.personalbest'),
        ),
    ]
