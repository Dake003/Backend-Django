# Generated by Django 4.2 on 2023-04-18 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tengri', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('text', models.TextField()),
            ],
        ),
    ]
