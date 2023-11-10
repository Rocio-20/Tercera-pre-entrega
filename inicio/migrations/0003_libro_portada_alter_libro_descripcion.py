# Generated by Django 4.2.7 on 2023-11-09 23:51

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_alter_editorial_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='portada',
            field=models.ImageField(null=True, upload_to='imagenes_libros/'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='descripcion',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
