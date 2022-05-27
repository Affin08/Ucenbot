# Generated by Django 4.0.4 on 2022-05-26 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_delete_intents'),
    ]

    operations = [
        migrations.CreateModel(
            name='Intents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=200)),
                ('pattern', models.CharField(max_length=200)),
                ('response', models.CharField(max_length=200)),
                ('context_set', models.CharField(max_length=200)),
            ],
        ),
    ]