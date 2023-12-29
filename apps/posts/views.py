from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from .models import Post, Comentario, Categoria
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .forms import ComentarioForm, CrearPostForm, NuevaCategoriaForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView
from django.contrib import messages

# Create your views here.



class PostListView(ListView):
    model = Post
    template_name = "post/posts.html"
    context_object_name = "posts"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        orden = self.request.GET.get('orden')
        if orden == 'reciente':
            queryset = queryset.order_by('-fecha')
        elif orden == 'antiguo':
            queryset = queryset.order_by('fecha')
        elif orden == 'alfabeto':
            queryset = queryset.order_by('titulo')
        return queryset
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['orden'] = self.request.GET.get('orden','reciente')
        context['categorias'] = Categoria.objects.all()
        return context 

class PostDetailView(DetailView):
    model = Post
    template_name = "post/post_individual.html"
    context_object_name = "posts"
    pk_url_kwarg = "id"
    queryset = Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ComentarioForm()
        context['comentarios'] = Comentario.objects.filter(posts_id=self.kwargs['id'])
        context['categorias'] = Categoria.objects.all()
        for comentario in context['comentarios']:
         comentario.usuario = comentario.usuario 
        return context
    
    def post(self, request, *args, **kwargs):
        form = ComentarioForm(request.POST)
        if form.is_valid():
               if request.user.is_authenticated: 
        
            
                  messages.success(self.request, 'Comentario creado con éxito.')
                  comentario = form.save(commit=False)
                  comentario.usuario = request.user 
                  comentario.posts_id = self.kwargs['id'] 
                  comentario.save()
            
                  return redirect('apps.posts:post_individual' , id = self.kwargs['id'] ) 
               else:
                 messages.error(self.request, 'Debes iniciar sesión para comentar.')
                 context = {'form': form}
                 return redirect('login')
            
        else:
            
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render(request, self.template_name, context) 
        
class ComentarioCreateView(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = ComentarioForm
    template_name = 'comentario/crear_comentario.html' 
    success_url= 'comentario/comentarios/'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        form.instance.posts_id = self.kwargs['posts_id'] 
        return super().form_valid(form)
    
    def get_success_url(self):
        messages.success(self.request, '¡Comentario creado!')
        return reverse('apps.posts:post_individual', args=[self.kwargs['id']])
    
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    form_class = CrearPostForm
    template_name = 'post/crear_post.html' 
    success_url= reverse_lazy('apps.posts:posts')
    
class CategoriaCreateView(LoginRequiredMixin,CreateView):
    model = Categoria
    form_class = NuevaCategoriaForm
    template_name = 'post/crear_categoria.html' 
    
    def get_success_url(self):
        messages.success(self.request, '¡Categoría creada con éxito!')
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        else: 
            return reverse_lazy('apps.posts:categoria_list')
        
class CategorialistView(ListView):
    model = Categoria
    template_name = 'post/categoria_list.html'
    context_object_name = 'categorias'
    

class CategoriaDeleteView(LoginRequiredMixin,DeleteView):
    model= Categoria
    template_name = 'post/categoria_confirm_delete.html'
    success_url = reverse_lazy('apps.posts:categoria_list')
    
class PostUpdateView(LoginRequiredMixin,UpdateView):
    model = Post
    form_class = CrearPostForm
    template_name = 'post/modificar_post.html'
    success_url = reverse_lazy('apps.posts:posts')





class PostDeleteView(LoginRequiredMixin,DeleteView):
    model= Post
    template_name = 'post/eliminar_post.html'
    success_url = reverse_lazy('apps.posts:posts')
    
class ComentarioUpdateView(LoginRequiredMixin,UpdateView):
    model = Comentario
    form_class = ComentarioForm
    template_name = 'comentario/comentario_form.html'
    
    def get_success_url(self):
        messages.success(self.request, '¡Comentario modificado con éxito!')
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        else:
            return reverse('apps.posts:post_individual',args=[self.object.posts.id])

class ComentarioDeleteView(LoginRequiredMixin, DeleteView):
    model = Comentario
  
    template_name = 'comentario/comentario_confirm_delete.html'

    def get_success_url(self):
        messages.success(self.request, '¡Comentario eliminado con éxito!')
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        else:
            return reverse_lazy('apps.posts:post_individual', args=[self.object.posts.id])
class PostsPorCategoria(ListView):
    model = Post
    template_name = 'post/posts_por_categoria.html'
    context_object_name = 'posts'
    
    def get_queryset(self):
        return Post.objects.filter(categoria_id=self.kwargs['pk'])
