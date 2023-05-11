# Generated by Django 4.1.7 on 2023-05-11 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Filter_Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(choices=[('$50 TO $100', '$50 TO $100'), ('$101 TO $150', '$101 TO $150'), ('$151 TO $200', '$151 TO $200'), ('$201 TO $300', '$201 TO $300')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=50)),
            ],
        ),
    ]