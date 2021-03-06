# Generated by Django 3.1.7 on 2021-03-19 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_auto_20210319_1020'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avg_rgb', models.CharField(max_length=100)),
                ('avg_image', models.ImageField(upload_to='')),
                ('height', models.IntegerField()),
                ('width', models.IntegerField()),
                ('file', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pages.uploadfile')),
            ],
        ),
    ]
