# Generated by Django 4.2.5 on 2023-09-19 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('idGenero', models.IntegerField(db_column='idGenero', primary_key=True, serialize=False)),
                ('tipoGenero', models.CharField(db_column='tipoGenero', max_length=100)),
            ],
            options={
                'db_table': 'Genero',
            },
        ),
    ]
