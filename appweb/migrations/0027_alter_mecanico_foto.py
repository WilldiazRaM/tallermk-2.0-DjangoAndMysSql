# Generated by Django 5.0.3 on 2024-03-26 03:38

import appweb.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0026_alter_contacto_fecha_alter_mecanico_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mecanico',
            name='foto',
            field=models.ImageField(null=True, upload_to=appweb.models.path_and_rename),
        ),
    ]
