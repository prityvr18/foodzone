# Generated by Django 4.2.5 on 2024-08-30 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_category_dish_team_alter_contact_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='facebook_url',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='team',
            name='twitter_url',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]