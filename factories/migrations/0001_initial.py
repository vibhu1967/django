# Generated by Django 2.1.15 on 2022-09-13 20:08

from django.db import migrations, models
import django.db.models.deletion
import factories.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('description', models.CharField(max_length=100, null=True)),
                ('image', models.ImageField(null=True, upload_to=factories.models.upload_path)),
                ('identity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relation', to='factories.Companies')),
            ],
        ),
    ]
