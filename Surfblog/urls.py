from django.urls import path
from Surfblog import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name = 'Inicio'),
    path('sobreNosotros/', views.sobreNostros, name = 'sobreNosotros'),
    path('hacerPost/', views.hacerPost, name = 'hacerPost'),
    path('post/<titulo>', views.abrirPost, name='Post'),
    path('buscar/', views.buscar, name = 'Buscar'),
    path('register/', views.registro, name = 'Register'),
    path('login/', views.iniciarSesion, name = 'Login'),
    path('logout/',  LogoutView.as_view(template_name = 'Surfblog/logout.html'), name = 'Logout'),
    path('listaPosteos/', views.listaPosteos, name = 'listaPosteos'),
    path('borrarPosteo/<posteo_titulo>', views.borrarPosteos, name = 'borrarPosteo'),
    path('editarPosteo/<posteo_titulo>', views.editarPosteos, name = 'editarPosteo'),
    path('editarUsuario/', views.editarUsuario, name = 'editarUsuario'),
    path('agregarAvatar/', views.agregarAvatar, name = 'agregarAvatar')
]
