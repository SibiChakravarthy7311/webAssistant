# Generated by Django 3.1.7 on 2021-04-26 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('task', models.CharField(max_length=20)),
            ],
        ),
    ]