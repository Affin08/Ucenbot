# Generated by Django 4.0.4 on 2022-05-04 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='inputclass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inputmsg', models.CharField(max_length=200)),
            ],
        ),
    ]
