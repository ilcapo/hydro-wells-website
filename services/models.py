# services/models.py
from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=100)
    # Campos nuevos con valores por defecto
    short_description = models.TextField(
        help_text="Breve descripción para mostrar en la lista de servicios",
        default="Servicio profesional"
    )
    full_description = models.TextField(
        help_text="Descripción completa para la página de detalle",
        default="Descripción del servicio"
    )
    benefit = models.TextField(
        blank=True,
        help_text="Beneficio principal del servicio",
        default="Beneficio principal del servicio"
    )
    requirements = models.TextField(
        blank=True,
        help_text="Requisitos o características (uno por línea)",
        default=""
    )
    
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    icon = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title

    def get_requirements_list(self):
        """Convierte el texto de requisitos en una lista"""
        if self.requirements:
            return [req.strip() for req in self.requirements.split('\n') if req.strip()]
        return []
