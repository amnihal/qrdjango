# Generated by Django 5.0.1 on 2024-01-20 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0002_delete_puzzleimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Puzzle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='puzzle')),
                ('Name', models.CharField(max_length=100)),
                ('row', models.IntegerField()),
                ('col', models.IntegerField()),
            ],
        ),
    ]
