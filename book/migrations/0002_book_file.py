# Generated by Django 5.1.2 on 2024-10-19 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='file',
            field=models.FileField(default=123, upload_to='book_files/'),
            preserve_default=False,
        ),
    ]
