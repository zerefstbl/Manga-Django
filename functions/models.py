from random import choices
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models

from django.contrib.auth.models import User

from django.utils import timezone

from multiselectfield import MultiSelectField


def user_picture_directory(instance, filename):
    return '{0}/{1}'.format(instance.user, filename)


def manga_directory_path(instance, filename):
    return '{0}/{1}/{2}'.format(instance.nome, instance.cap_number, filename)


def banner_directory_path(instance, filename):
    return '{0}/{1}'.format(instance.nome, filename)


@receiver(post_save, sender=User)
def create_profile(sender, created, instance, **kwargs):
    if created:
        Profile.objects.create(user=instance)


class Manga(models.Model):
    nome = models.CharField(max_length=100)
    teste = models.ManyToManyField(
        'NewCap', related_name="testezin")
    descricao = models.TextField(max_length=500)
    capa = models.ImageField(upload_to=banner_directory_path)
    created_on = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(
        User, related_name='liked', blank=True, null=True)
    banner = models.ImageField(
        upload_to=banner_directory_path, blank=True, null=True)
    categorias = MultiSelectField(blank=True, null=True, choices=(
        ('AC', 'Ação'),
        ('AV', 'Aventura'),
        ('IS', 'Isekai'),
        ('FT', 'Fantansia'),
        ('HT', 'Hentai'),
        ('EC', 'Ecchi'),
        ('CT', 'Cultivação'),
    ))

    def __str__(self):
        return self.nome


class NewCap(models.Model):
    cap_number = models.PositiveIntegerField()
    images = models.ManyToManyField('Images')
    manga = models.ForeignKey('Manga', on_delete=models.CASCADE)
    update_on = models.DateTimeField(auto_now=True, blank=True, null=True)
    likes = models.ManyToManyField(
        User, related_name='+', blank=True, null=True)


class Images(models.Model):
    image = models.ImageField(upload_to=manga_directory_path)
    nome = models.ForeignKey(Manga, on_delete=models.CASCADE)
    cap_number = models.PositiveIntegerField(blank=True, null=True)


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile', verbose_name='user')
    salvos = models.ManyToManyField(
        'Manga', blank=True, null=True, related_name='salvos')
    favoritos = models.ManyToManyField(
        'Manga', related_name='favoritados', blank=True, null=True)
    picture = models.ImageField(
        upload_to=user_picture_directory, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    seguidores = models.ManyToManyField(User, related_name='followers')
