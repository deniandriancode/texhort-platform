# Generated by Django 5.0.6 on 2024-05-17 07:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('texhort', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_content', models.CharField(max_length=400)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='texhort.author')),
                ('paragraph', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='texhort.paragraph')),
            ],
        ),
    ]
