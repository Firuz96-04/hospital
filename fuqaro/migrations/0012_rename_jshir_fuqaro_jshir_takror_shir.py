# Generated by Django 4.0.4 on 2022-05-08 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fuqaro', '0011_alter_chetelfuqarosi_vaqtinchalik_kucha_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fuqaro_jshir_takror',
            old_name='jshir',
            new_name='shir',
        ),
    ]
