# Generated by Django 2.2 on 2019-04-25 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graoh', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.IntegerField(default=0)),
                ('price', models.PositiveIntegerField(default=0)),
                ('last_modify_date', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('version', models.IntegerField(default=0)),
            ],
        ),
    ]