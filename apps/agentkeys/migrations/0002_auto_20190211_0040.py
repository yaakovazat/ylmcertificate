# Generated by Django 2.1.5 on 2019-02-10 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agentkeys', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agent',
            old_name='wecaht',
            new_name='wechat',
        ),
    ]
