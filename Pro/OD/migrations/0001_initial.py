# Generated by Django 3.1.2 on 2021-03-09 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ODList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SNo', models.IntegerField()),
                ('RollNo', models.CharField(max_length=100)),
                ('Name', models.CharField(max_length=100)),
                ('ClassAdvisor', models.CharField(max_length=100)),
                ('Type', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'ODs',
            },
        ),
    ]
