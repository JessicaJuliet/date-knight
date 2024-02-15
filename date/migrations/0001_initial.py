# Generated by Django 4.2.8 on 2024-02-15 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DateIdea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('budget', models.SmallIntegerField(choices=[(1, 'Low'), (2, 'Medium'), (3, 'High')])),
                ('place', models.CharField(choices=[('restaurant', 'Restaurant'), ('park', 'Park'), ('museum', 'Museum'), ('movie', 'Movie'), ('bar', 'Bar'), ('other', 'Other')], max_length=200)),
                ('preferences', models.ManyToManyField(related_name='date_ideas', to='date.preference')),
            ],
        ),
    ]
