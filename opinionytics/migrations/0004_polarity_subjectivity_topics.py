# Generated by Django 2.1.dev20180503070829 on 2018-05-22 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opinionytics', '0003_popularity_concept'),
    ]

    operations = [
        migrations.CreateModel(
            name='Polarity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('polarity', models.CharField(max_length=50)),
                ('confidence', models.DecimalField(decimal_places=1, max_digits=2)),
            ],
        ),
        migrations.CreateModel(
            name='Subjectivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjectivity', models.CharField(max_length=50)),
                ('confidence', models.DecimalField(decimal_places=1, max_digits=2)),
            ],
        ),
        migrations.CreateModel(
            name='Topics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topics', models.CharField(max_length=50)),
                ('confidence', models.DecimalField(decimal_places=1, max_digits=2)),
            ],
        ),
    ]
