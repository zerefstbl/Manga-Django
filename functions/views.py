from operator import is_
from django.db.models import Q
from django.http import JsonResponse
from .models import Profile
from logging import captureWarnings
from django.shortcuts import render, redirect

from django.contrib.auth.models import User

from django.views.generic import View

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Manga, Images, NewCap

from .forms import MangaForm, CapForm


class HomeView(View):
    def get(self, request, *args, **kwargs):

        mangas = Manga.objects.all().order_by('?')

        ultima_atualizacao = NewCap.objects.all().order_by('-update_on')

        if request.user.is_authenticated:
            profile = Profile.objects.get(user=request.user)

            salvos = profile.salvos.all()

            context = {'mangas': mangas,
                       'ult_atts': ultima_atualizacao,
                       'salvos': salvos,
                       'profile': profile,
                       }
        else:
            context = {'mangas': mangas,
                       'ult_atts': ultima_atualizacao,
                       }

        return render(request, 'functions/home.html', context)

    def post(self, request, *args, **kwargs):
        return render(request, 'functions/home.html')


class MangaView(View):
    def get(self, request, pk, *args, **kwargs):

        manga = Manga.objects.get(pk=pk)

        caps = NewCap.objects.filter(manga=manga).order_by('-id')

        mangas = Manga.objects.all().order_by('?')

        context = {
            'manga': manga,
            'caps': caps,
            'mangas': mangas,
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

        capslok = NewCap.objects.get(
            manga=manga, cap_number=kwargs['cap_number'])

        print(capslok.id)

        caps = capslok.images.all().order_by('-pk')

        proximo = capslok.cap_number + 1

        anterior = capslok.cap_number - 1

        context = {'manga': manga, 'caps': caps,
                   'proximo': proximo, 'anterior': anterior, 'post': capslok, }

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
            img = Images(image=file, nome=manga,
                         cap_number=request.POST.get('cap_number'))
            img.save()
            new_post.images.add(img)

        manga.teste.add(new_post)

        return redirect('home-view')


class SaveManga(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):

        manga = Manga.objects.get(pk=pk)
        profile = Profile.objects.get(user=request.user)

        mangas = profile.salvos.all()
        print(mangas)

        if manga in mangas:
            profile.salvos.remove(manga)
        else:
            profile.salvos.add(manga)

        return redirect('home-view')


class ProfileView(View):
    def get(self, request, pk, *args, **kwargs):

        profile = Profile.objects.get(pk=pk)

        context = {
            'profile': profile,
        }

        return render(request, 'functions/profile.html', context)


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def search(request):
    if is_ajax(request=request):
        res = None
        series = request.POST.get('series')
        print(series)
        results = Manga.objects.filter(nome__icontains=series)

        if len(series) > 0 and len(results) > 0:
            data = []
            for mang in results:
                item = {
                    'manga_nome': mang.nome,
                    'image': mang.capa.url,
                    'pk': mang.pk,
                }
                data.append(item)
            res = data
        else:
            res = 'Nenhum Manga encontrado!!'

        return JsonResponse({'data': res})

    return JsonResponse({})


class AddLikeView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):

        manga = NewCap.objects.get(pk=pk)

        user = request.user

        likes = manga.likes.all()

        is_like = False

        if user in likes:
            manga.likes.remove(user)
            is_like = False
        else:
            manga.likes.add(user)
            is_like = True

        return redirect('home-view')
