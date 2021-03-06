# Generated by Django 3.2.6 on 2021-08-31 13:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('words', '0015_alter_wordencounter_encounter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wordencounter',
            name='encounter',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='wordencounter',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='wordencounter',
            name='word_form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='word_encounter', to='words.wordforms'),
        ),
    ]
