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
        'featured_services': featured_services
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
            
    return render(request, 'home/contact.html')

def about_view(request):
    return render(request, 'home/about.html')
def faq_view(request):
    return render(request, 'home/faq.html')


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
    }
    return render(request, 'home/blog_detail.html', context)