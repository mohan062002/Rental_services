# Generated by Django 4.0.5 on 2022-11-29 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_rooms_p_email_alter_contact_c_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='owner_mobile',
            field=models.IntegerField(default=0),
        ),
    ]