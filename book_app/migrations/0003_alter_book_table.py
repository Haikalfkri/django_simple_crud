# Generated by Django 4.2.1 on 2023-06-04 00:54

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("book_app", "0002_alter_book_table"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="book",
            table="Book",
        ),
    ]