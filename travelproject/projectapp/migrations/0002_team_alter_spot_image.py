# Generated by Django 4.1.2 on 2022-11-02 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='spot',
            name='Image',
            field=models.ImageField(upload_to='pics'),
        ),
    ]
