# Generated by Django 3.2.6 on 2021-08-05 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rules', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rules',
            options={'verbose_name': 'Rule', 'verbose_name_plural': 'Rules'},
        ),
        migrations.AddField(
            model_name='rules',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
    ]
