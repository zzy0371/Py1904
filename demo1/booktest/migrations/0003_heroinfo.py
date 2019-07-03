# Generated by Django 2.2.1 on 2019-07-02 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0002_bookinfo_pub_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('gender', models.BooleanField(default=True)),
                ('content', models.CharField(max_length=100)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booktest.BookInfo')),
            ],
        ),
    ]