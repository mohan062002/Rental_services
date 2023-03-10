# Generated by Django 4.1.3 on 2022-11-27 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0002_delete_collections'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=50)),
                ('c_email', models.EmailField(max_length=200)),
                ('c_msg', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(max_length=50)),
                ('owner_username', models.CharField(max_length=30)),
                ('owner_email', models.EmailField(max_length=100)),
                ('owner_passward', models.CharField(max_length=50)),
                ('owner_confirmpass', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_type', models.CharField(max_length=20)),
                ('p_name', models.CharField(max_length=50)),
                ('p_adress', models.CharField(max_length=100)),
                ('p_city', models.CharField(max_length=50)),
                ('vacancy', models.IntegerField(default=0)),
                ('p_monthly', models.IntegerField()),
                ('p_facilities', models.CharField(max_length=100)),
                ('p_img', models.ImageField(default='', upload_to='user/images')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('user_username', models.CharField(max_length=30)),
                ('user_email', models.EmailField(max_length=100)),
                ('user_city', models.CharField(max_length=50)),
                ('user_passward', models.CharField(max_length=16)),
                ('user_confirmpass', models.CharField(max_length=16)),
            ],
        ),
    ]
