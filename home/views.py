# home/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from services.models import Service
from django.core.paginator import Paginator
from .models import BlogPost, BlogCategory

def index(request):
    # Obtener los primeros 3 servicios para mostrar en la home
    featured_services = Service.objects.all()[:3] # Puedes ajustar este número
    # Pasamos los servicios al template
     
    context = {
        'featured_services': featured_services,
        'meta_title': 'HydroWells - Perforación de Pozos y Reparación de Bombas en Maryland',
        'meta_description': 'Servicios profesionales de perforación de pozos, reparación de bombas y mantenimiento de sistemas de agua en Maryland. Emergencias 24/7.',
        'meta_keywords': 'perforación de pozos Maryland, reparación de bombas, mantenimiento de pozos, emergencia de pozos, servicios de agua Maryland',
    }
    return render(request, 'home/index.html', context)

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        full_message = f"""
        Nuevo mensaje de contacto desde la web HydroWells:
        
        Nombre: {name}
        Email: {email}
        Asunto: {subject}
        
        Mensaje:
        {message}
        """
        
        try:
            send_mail(
                f"HydroWells Contacto: {subject}",
                full_message,
                email,
                [settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )
            messages.success(request, '¡Gracias! Tu mensaje ha sido enviado exitosamente.')
            return redirect('contact')
        except Exception as e:
            messages.error(request, 'Oops! Hubo un error al enviar tu mensaje. Por favor inténtalo de nuevo.')

        
        # Diccionario de traducciones
        translations = {
            'es': {
                'meta_title': 'Contacto - HydroWells Servicios de Pozos',
                'meta_description': 'Contáctanos para servicios profesionales de pozos de agua en Maryland. Disponible 24/7 para emergencias. Obtén tu cotización gratuita.',
                'meta_keywords': 'contacto pozos de agua, emergencia de pozos, cotización de pozos, Maryland, servicios de pozos',
            },
            'en': {
                'meta_title': 'Contact - HydroWells Water Well Services',
                'meta_description': 'Contact us for professional water well services in Maryland. Available 24/7 for emergencies. Get your free quote.',
                'meta_keywords': 'water well contact, well emergency, well quote, Maryland, well services',
            }
        }
        
        # Por ahora fijo en español, luego puedes detectar el idioma
        lang = 'es'  # o 'en'
        
        context = translations[lang]
    return render(request, 'home/contact.html')


def about_view(request):
    # Diccionario de traducciones
    translations = {
        'es': {
            'meta_title': 'Acerca de HydroWells - Expertos en Pozos de Agua',
            'meta_description': 'Conoce a nuestro equipo de expertos en perforación de pozos y reparación de bombas en Maryland. Nuestra experiencia y compromiso con la calidad nos hacen líderes en el sector.',
            'meta_keywords': 'acerca de HydroWells, equipo de pozos, expertos en pozos, historia de HydroWells, servicios de pozos Maryland',
        },
        'en': {
            'meta_title': 'About HydroWells - Water Well Experts',
            'meta_description': 'Meet our team of experts in well drilling and pump repair in Maryland. Our experience and commitment to quality make us leaders in the industry.',
            'meta_keywords': 'about HydroWells, well team, well experts, HydroWells history, Maryland well services',
        }
    }
    
    # Por ahora fijo en español, luego puedes detectar el idioma
    lang = 'es'  # o 'en'
    
    context = translations[lang]
    return render(request, 'home/about.html', context)

def faq_view(request):
     # Diccionario de traducciones
    translations = {
        'es': {
            'meta_title': 'Preguntas Frecuentes sobre Pozos de Agua - HydroWells',
            'meta_description': 'Respuestas a las preguntas más comunes sobre pozos de agua, perforación, bombas y mantenimiento en Maryland.',
            'meta_keywords': 'FAQ pozos de agua, preguntas sobre pozos, mantenimiento de pozos, Maryland, guía de pozos',
        },
        'en': {
            'meta_title': 'Frequently Asked Questions about Water Wells - HydroWells',
            'meta_description': 'Answers to the most common questions about water wells, drilling, pumps, and maintenance in Maryland.',
            'meta_keywords': 'water well FAQ, well questions, well maintenance, Maryland, well guide',
        }
    }
    
    # Determinar el idioma (por ahora fijo, después se puede detectar)
    lang = 'es'  # o 'en'
    
    context = translations[lang]
    return render(request, 'home/faq.html', context)


def blog_list(request):
    posts = BlogPost.objects.filter(is_published=True)
    categories = BlogCategory.objects.all()
    
    # Filtro por categoría
    category_slug = request.GET.get('category')
    if category_slug:
        category = get_object_or_404(BlogCategory, slug=category_slug)
        posts = posts.filter(category=category)
    
    # Paginación
    paginator = Paginator(posts, 6) # 6 posts por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'categories': categories,
        'posts': posts,
        'meta_title': 'Water Well Blog - Tips and Guides - HydroWells',
        'meta_description': 'Professional water well blog: maintenance tips, technical guides, news, and experts on water systems in Maryland.',
        'meta_keywords': 'Water well blog, well tips, well maintenance, well technical guide, Maryland.',
    
    }
    return render(request, 'home/blog_list.html', context)

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, is_published=True)
    related_posts = BlogPost.objects.filter(
        category=post.category, 
        is_published=True
    ).exclude(id=post.id)[:3] # 3 posts relacionados
    
    context = {
        'post': post,
        'related_posts': related_posts,
         'post': post,
        'meta_title': f'{post.title} - Blog HydroWells',
        'meta_description': post.excerpt[:155] if post.excerpt else post.title,
        'meta_keywords': f'{post.title.lower()}, pozos de agua, Maryland,',
    
    }
    return render(request, 'home/blog_detail.html', context)