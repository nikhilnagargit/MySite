# Generated by Django 3.0.5 on 2020-04-10 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_auto_20200410_0946'),
    ]

    operations = [
        migrations.RenameField(
            model_name='certificate',
            old_name='image',
            new_name='gdrivelink',
        ),
    ]