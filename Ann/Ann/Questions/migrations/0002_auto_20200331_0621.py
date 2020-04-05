# Generated by Django 3.0.4 on 2020-03-31 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Questions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='correct',
            field=models.CharField(default='none', max_length=200),
        ),
        migrations.AddField(
            model_name='questions',
            name='marks',
            field=models.IntegerField(choices=[(2, 2), (4, 4), (6, 6)], default=4),
        ),
    ]