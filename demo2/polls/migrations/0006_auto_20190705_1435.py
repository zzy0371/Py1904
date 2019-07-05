# Generated by Django 2.2.1 on 2019-07-05 06:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0005_auto_20190705_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temp',
            name='desc',
            field=models.CharField(blank=True, db_column='描述', help_text='描述', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='temp',
            name='title',
            field=models.CharField(help_text='标题', max_length=20, verbose_name='标题'),
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telephone', models.CharField(max_length=11)),
                ('default_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
