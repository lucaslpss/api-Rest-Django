# Generated by Django 4.1.3 on 2022-11-14 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=20)),
                ('senha', models.CharField(blank=True, max_length=20, null=True)),
                ('data_nascimento', models.DateField()),
            ],
        ),
    ]
