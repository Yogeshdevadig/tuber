# Generated by Django 3.1.1 on 2021-03-11 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0004_team_y_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUsForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('company_name', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=150)),
                ('details', models.TextField()),
            ],
        ),
    ]