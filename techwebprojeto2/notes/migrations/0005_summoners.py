# Generated by Django 4.2 on 2023-05-04 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_note_imagem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Summoners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summoner', models.TextField()),
            ],
        ),
    ]
