# Generated by Django 3.2.6 on 2021-08-30 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0014_wordencounter_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wordencounter',
            name='encounter',
            field=models.IntegerField(max_length=250),
        ),
    ]
