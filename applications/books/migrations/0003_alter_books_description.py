# Generated by Django 4.1.3 on 2022-12-04 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_books_options_remove_books_descriptions_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='description',
            field=models.TextField(blank=True, default=100, null=True),
        ),
    ]
