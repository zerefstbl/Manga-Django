from django.urls import path

from . import views 

urlpatterns = [
    path('', views.HomeView.as_view(), name='home-view'),
    path('manga/<int:pk>', views.MangaView.as_view(), name='manga-detail'),
    path('manga/<int:pk>/<int:cap_number>', views.CapView.as_view(), name='cap-view'),
    path('cadastro/', views.CadastrarManga.as_view(), name='cadastrar-manga'),
    path('cadastro-cap/<int:pk>', views.CadastrarCap.as_view(), name='cadastrar-cap'),
]
