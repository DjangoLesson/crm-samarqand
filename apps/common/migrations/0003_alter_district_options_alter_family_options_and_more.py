# Generated by Django 4.0.3 on 2022-04-26 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_mahalla_section'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='district',
            options={'verbose_name': 'Tuman', 'verbose_name_plural': 'Tuman'},
        ),
        migrations.AlterModelOptions(
            name='family',
            options={'verbose_name': 'Oila', 'verbose_name_plural': 'Oila'},
        ),
        migrations.AlterModelOptions(
            name='familymember',
            options={'verbose_name': 'Oila a`zolari', 'verbose_name_plural': 'Oila a`zolari'},
        ),
        migrations.AlterModelOptions(
            name='house',
            options={'verbose_name': 'Xonadon', 'verbose_name_plural': 'Xonadon'},
        ),
        migrations.AlterModelOptions(
            name='mahalla',
            options={'verbose_name': 'Mahalla', 'verbose_name_plural': 'Mahalla'},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Fuqoro', 'verbose_name_plural': 'Fuqoro'},
        ),
        migrations.AlterModelOptions(
            name='street',
            options={'verbose_name': 'Ko`cha', 'verbose_name_plural': 'Ko`cha'},
        ),
    ]
