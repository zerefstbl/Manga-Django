from django.db import models

from django.contrib.auth.models import User

from django.utils import timezone

def manga_directory_path(instance, filename):
    return '{0}/{1}/{2}'.format(instance.nome, instance.cap_number, filename)

def banner_directory_path(instance, filename):
    return '{0}/{1}'.format(instance.nome, filename)



class Manga(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.CharField(
        max_length=20,
        choices=(
            ('AC', 'Ação'),
            ('AV', 'Aventura'),
            ('IS', 'Isekai'),
            ('FT', 'Fantansia'),
            ('HT', 'Hentai'),
            ('EC', 'Ecchi'),
            ('CT', 'Cultivação'),
        )
    )
    descricao = models.TextField(max_length=500)
    capa = models.ImageField(upload_to=banner_directory_path)
    created_on = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, related_name='liked', blank=True, null=True)
    favoritos = models.ManyToManyField(User, related_name='favoritados', blank=True, null=True)
    banner = models.ImageField(upload_to=banner_directory_path, blank=True, null=True)


    def __str__(self):
        return self.nome
    

class NewCap(models.Model):
    cap_number = models.PositiveIntegerField()
    images = models.ManyToManyField('Images')
    manga = models.ForeignKey('Manga', on_delete=models.CASCADE)


class Images(models.Model):
    image = models.ImageField(upload_to=manga_directory_path)
    nome = models.ForeignKey(Manga, on_delete=models.CASCADE)
    cap_number = models.PositiveIntegerField(blank=True, null=True)