# Generated by Django 3.2.6 on 2021-08-23 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0005_auto_20210818_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wordforms',
            name='word',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='words.lemma'),
        ),
    ]
