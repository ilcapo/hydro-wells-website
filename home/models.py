# home/models.py
import json
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
import logging

class BlogCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    excerpt = models.TextField(max_length=300, help_text="Breve descripción para la lista de artículos")
    content = models.TextField(help_text="Contenido principal del artículo")
    structured_content = models.TextField(
        blank=True, 
        help_text="Contenido estructurado en formato JSON (por ejemplo, lista de mitos)",
        null=True
    )
    image = models.ImageField(upload_to='blog/images/', blank=True, null=True)
    category = models.ForeignKey(BlogCategory, on_delete=models.SET_NULL, null=True, blank=True)
    author = models.CharField(max_length=100, default="HydroWells Team")
    published_date = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=False)
    meta_description = models.CharField(max_length=160, blank=True, help_text="Para SEO")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'slug': self.slug})

    def get_structured_content(self):
        """Devuelve el contenido estructurado como diccionario"""
        if self.structured_content:
            try:
                parsed_content = json.loads(self.structured_content)
                # print(f"DEBUG: Contenido estructurado parseado: {parsed_content}") # Opcional: print para depurar
                # Si el JSON es una lista directamente (como en tu ejemplo)
                if isinstance(parsed_content, list):
                    return {"items": parsed_content}
                # Si el JSON es un diccionario con una clave 'content' (como en tu ejemplo)
                elif isinstance(parsed_content, dict) and 'content' in parsed_content:
                    return {"items": parsed_content['content']}
                # Si el JSON ya es un diccionario con 'items'
                elif isinstance(parsed_content, dict) and 'items' in parsed_content:
                    return parsed_content
                else:
                    # print(f"DEBUG: Formato de contenido estructurado inesperado: {type(parsed_content)}") # Opcional
                    return parsed_content
            except json.JSONDecodeError:
                # print(f"ERROR: Error al decodificar JSON para el post {self.id}") # Opcional
                return {}
        # print("DEBUG: No hay contenido estructurado") # Opcional
        return {}

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_date']