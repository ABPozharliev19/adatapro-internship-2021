# Generated by Django 3.2.5 on 2021-07-25 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HistoryScraping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.CharField(max_length=256)),
                ('price', models.FloatField(max_length=32)),
                ('date', models.DateField(auto_now=True)),
                ('site_link', models.URLField(max_length=512)),
            ],
            options={
                'managed': True,
            },
        ),
    ]