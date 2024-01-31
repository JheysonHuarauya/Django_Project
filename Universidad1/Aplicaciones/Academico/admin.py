from django.contrib import admin
from .models import Carrera, Estudiante, Profesor, Curso, Matricula
# Register your models here.
admin.site.register(Carrera)
admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Curso)
admin.site.register(Matricula)
