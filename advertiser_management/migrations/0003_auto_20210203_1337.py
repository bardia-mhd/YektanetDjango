# Generated by Django 3.1.5 on 2021-02-03 13:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.datetime_safe


class Migration(migrations.Migration):

    dependencies = [
        ('advertiser_management', '0002_ad_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ad',
            name='clicks',
        ),
        migrations.RemoveField(
            model_name='ad',
            name='views',
        ),
        migrations.RemoveField(
            model_name='advertiser',
            name='clicks',
        ),
        migrations.RemoveField(
            model_name='advertiser',
            name='views',
        ),
        migrations.AddField(
            model_name='ad',
            name='approve',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='ad',
            name='link',
            field=models.URLField(max_length=300),
        ),
        migrations.CreateModel(
            name='View',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(default=django.utils.datetime_safe.datetime.now)),
                ('user_ip', models.GenericIPAddressField()),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advertiser_management.ad')),
            ],
        ),
        migrations.CreateModel(
            name='Click',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(default=django.utils.datetime_safe.datetime.now)),
                ('user_ip', models.GenericIPAddressField()),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advertiser_management.ad')),
            ],
        ),
    ]
