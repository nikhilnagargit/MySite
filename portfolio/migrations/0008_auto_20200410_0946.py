# Generated by Django 3.0.5 on 2020-04-10 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_certificate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='image',
            field=models.URLField(max_length=10000),
        ),
    ]
