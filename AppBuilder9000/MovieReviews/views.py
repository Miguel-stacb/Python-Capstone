from django.shortcuts import render, redirect, get_object_or_404
from .forms import MovieForm
from .models import Movie
from django.core.paginator import Paginator
from django.contrib import messages


def home(request):
    # Obtener todas las películas
    all_movies = Movie.objects.all()

    # Obtener películas con alta calificación
    high_rated_movies = Movie.objects.high_rated()

    # Obtener películas recientes
    recent_movies = Movie.objects.recent_releases()

    context = {
        'all_movies': all_movies,
        'high_rated_movies': high_rated_movies,
        'recent_movies': recent_movies,
    }
    return render(request, 'MovieReviews/home.html', context)

def contact(request):
    return render(request, 'MovieReviews/contact.html')



def index(request):
    return render(request, 'AppBuilder9000/Home/index.html')

def create_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('MovieReviews:home')  # Redirige a la página de inicio después de guardar
    else:
        form = MovieForm()
    return render(request, 'MovieReviews/create_movie.html', {'form': form})


def items_list(request):
    # Obtener todos los objetos de la base de datos
    items = Movie.objects.all()

    # Implementar la búsqueda si se proporciona un término de búsqueda
    query = request.GET.get('q')
    if query:
        items = items.filter(title__icontains=query)

    # Configurar la paginación
    paginator = Paginator(items, 10)  # Mostrar 10 items por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'MovieReviews/items_list.html', {'items': page_obj.object_list, 'page_obj': page_obj})

def item_details(request, item_id):
    item = get_object_or_404(Movie, id=item_id)
    return render(request, 'MovieReviews/item_details.html', {'item': item})

def item_edit(request, item_id):
    item = get_object_or_404(Movie, id=item_id)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('MovieReviews:item_details', item_id=item.id)
    else:
        form = MovieForm(instance=item)
    return render(request, 'MovieReviews/item_edit.html', {'form': form, 'item': item})

def item_delete(request, item_id):
    item = get_object_or_404(Movie, id=item_id)
    if request.method == 'POST':
        item.delete()
        messages.success(request, 'Item deleted successfully.')
        return redirect('MovieReviews:items_list')
    return render(request, 'MovieReviews/item_delete.html', {'item': item})