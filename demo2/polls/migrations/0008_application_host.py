# Generated by Django 2.2.1 on 2019-07-05 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_account_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('h', models.ManyToManyField(to='polls.Host')),
            ],
        ),
    ]
