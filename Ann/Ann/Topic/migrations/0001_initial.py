# Generated by Django 3.0.4 on 2020-03-30 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Subject', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Subject.Subject')),
            ],
        ),
    ]
