# Generated by Django 4.0.5 on 2022-06-18 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Athlete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('birthday', models.DateTimeField()),
                ('sex', models.CharField(choices=[('М', 'Male'), ('Ж', 'Female')], default='М', max_length=1)),
                ('style', models.CharField(choices=[('кроль', 'Freestyle'), ('дельфин', 'Butterfly'), ('на спине', 'Backstroke'), ('брасс', 'Breaststroke'), ('комплекс', 'Medley')], default='кроль', max_length=16)),
            ],
        ),
    ]
