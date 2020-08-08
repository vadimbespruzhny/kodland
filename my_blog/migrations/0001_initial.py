# Generated by Django 3.0.8 on 2020-08-04 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('text', models.CharField(max_length=500, verbose_name='Текст поста')),
                ('img', models.ImageField(upload_to='', verbose_name='Картинка поста')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
