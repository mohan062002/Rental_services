# Generated by Django 4.0.5 on 2022-11-16 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='collections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection_title', models.CharField(max_length=50)),
                ('collection_desc', models.CharField(max_length=100)),
                ('collection_image', models.ImageField(default='', upload_to='manna/images')),
            ],
        ),
    ]
