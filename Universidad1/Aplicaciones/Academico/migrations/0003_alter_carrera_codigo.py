# Generated by Django 5.0.1 on 2024-01-24 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academico', '0002_carrera_curso_salon_estudiante_matricula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrera',
            name='codigo',
            field=models.CharField(max_length=4, primary_key=True, serialize=False),
        ),
    ]
