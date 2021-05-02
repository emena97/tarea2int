# Generated by Django 3.1.7 on 2021-05-01 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Albums',
            fields=[
                ('id', models.CharField(max_length=22, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('genre', models.CharField(max_length=300)),
                ('artist_id', models.CharField(max_length=22)),
                ('artist', models.CharField(max_length=300)),
                ('tracks', models.CharField(max_length=300)),
                ('self', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Artists',
            fields=[
                ('id', models.CharField(max_length=22, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('albums', models.CharField(max_length=300)),
                ('tracks', models.CharField(max_length=300)),
                ('self', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Tracks',
            fields=[
                ('id', models.CharField(max_length=22, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('duration', models.FloatField()),
                ('times_played', models.IntegerField()),
                ('album_id', models.CharField(max_length=22)),
                ('artist', models.CharField(max_length=300)),
                ('album', models.CharField(max_length=300)),
                ('self', models.CharField(max_length=300)),
            ],
        ),
    ]
