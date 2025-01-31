# Generated by Django 5.1.5 on 2025-01-21 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grid', models.JSONField()),
                ('width', models.IntegerField(default=50)),
                ('height', models.IntegerField(default=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
