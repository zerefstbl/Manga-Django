from django.shortcuts import render, redirect

from django.contrib.auth.models import User

from django.views.generic import View

from .models import Manga, Images, NewCap

from .forms import MangaForm, CapForm

class HomeView(View):
    def get(self, request, *args, **kwargs):

        mangas = Manga.objects.all()

        context = {'mangas': mangas,}


        return render(request, 'functions/home.html', context)
        
    def post(self, request, *args, **kwargs):
        return render(request, 'functions/home.html')

class MangaView(View):
    def get(self, request, pk, *args, **kwargs):

        manga = Manga.objects.get(pk=pk)

        caps = NewCap.objects.filter(manga=manga).order_by('-id')


        context = {
            'manga': manga,
            'caps': caps,
        }

        return render(request, 'functions/manga-view.html', context)


    def post(self, request, pk, *args, **kwargs):

        add_like = Manga.objects.get(pk=pk)

        likes = add_like.likes.all()

        is_like = False

        for like in likes:
            if like == request.user:
                is_like = True
                break
            else:
                add_like.likes.add(request.user)

        return redirect('manga-detail', pk=pk)

        
    

class CapView(View):
    def get(self, request, pk, *args, **kwargs):
        
        manga = Manga.objects.get(pk=pk)

        capslok = NewCap.objects.get(manga=manga, cap_number=kwargs['cap_number'])
        caps = capslok.images.all().order_by('-pk')
        proximo = capslok.cap_number + 1
        anterior = capslok.cap_number - 1
        context = {'manga': manga, 'caps': caps, 'proximo': proximo, 'anterior': anterior,}
        
        return render(request, 'functions/cap-view.html', context)
        

class CadastrarManga(View):
    def get(self, request, *args, **kwargs):
        form = MangaForm()

        context = {'form': form}

        return render(request, 'functions/cadastrar-manga.html', context)

    
    def post(self, request, *args, **kwargs):

        form = MangaForm(request.POST, request.FILES)

        if form.is_valid():
            new_post = form.save()


        return redirect('home-view')


class CadastrarCap(View):
    def get(self, request, pk, *args, **kwargs):

        manga = Manga.objects.get(pk=pk)

        form = CapForm()

        context = {
            'form': form,
        }


        return render(request, 'functions/cadastrar-manga.html', context)


    def post(self, request, pk, *args, **kwargs):

        manga = Manga.objects.get(pk=pk)

        form = CapForm(request.POST, request.FILES)

        files = request.FILES.getlist('image')

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.manga = manga
            new_post.save()

        for file in files:
            img = Images(image=file, nome=manga, cap_number=request.POST.get('cap_number'))
            img.save()
            new_post.images.add(img)
        


        return redirect('home-view')

