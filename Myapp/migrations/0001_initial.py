# Generated by Django 4.2.7 on 2024-01-02 05:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryname', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('company_name', models.CharField(max_length=200)),
                ('experience', models.PositiveIntegerField()),
                ('salary', models.PositiveIntegerField()),
                ('qualification', models.CharField(max_length=200)),
                ('skills', models.CharField(max_length=200)),
                ('poster', models.ImageField(upload_to='poster')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Myapp.category')),
            ],
        ),
    ]
