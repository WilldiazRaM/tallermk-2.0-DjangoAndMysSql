# Generated by Django 5.0.3 on 2024-03-27 03:56

import appweb.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0037_alter_contacto_telefono_alter_mecanico_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='telefono',
            field=models.CharField(default='+569', help_text='Ingrese el número de teléfono válido.\n Nos pondremos en contacto con usted.\n  GarajelosHermanos.cl', max_length=12, validators=[django.core.validators.MinLengthValidator(limit_value=12, message='El número de teléfono debe tener al menos 12 caracteres.'), appweb.models.validate_integer]),
        ),
        migrations.AlterField(
            model_name='mecanico',
            name='foto',
            field=models.ImageField(null=True, upload_to=appweb.models.path_and_rename),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='telefono_cliente',
            field=models.CharField(default='+569', help_text='Ingrese el número de teléfono válido.\n Nos pondremos en contacto con usted. \n GarajelosHermanos.cl', max_length=12, validators=[django.core.validators.MinLengthValidator(limit_value=12, message='El número de teléfono debe tener al menos 12 caracteres.'), appweb.models.validate_integer]),
        ),
    ]
