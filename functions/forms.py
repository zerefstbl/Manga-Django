from django import forms

from .models import Manga, NewCap, Images


class MangaForm(forms.ModelForm):
    class Meta:
        model = Manga
        fields = '__all__'
        exclude = ['likes', 'favoritos', 'created_on', 'teste']


class CapForm(forms.ModelForm):
    image = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={
        'multiple': True
    }))

    class Meta:
        model = NewCap
        fields = '__all__'
        exclude = ['images', 'manga', ]
