# Generated by Django 2.1.5 on 2019-02-28 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Card', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card_shere',
            old_name='picture',
            new_name='img',
        ),
    ]