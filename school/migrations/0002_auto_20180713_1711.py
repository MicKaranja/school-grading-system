# Generated by Django 2.0.7 on 2018-07-13 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
    ]