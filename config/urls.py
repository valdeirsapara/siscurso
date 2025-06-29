"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from curso.views import listar_cursos, detalhe_curso
from core.views import home
from contrib.views import login_view, create_user_view
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
from curso import views as curso_views

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', home, name='home'),
    path('cursos/', listar_cursos, name='listar_cursos'),
    path('cursos/<int:curso_id>/', detalhe_curso, name='detalhe_curso'),
    path('cursos/novo/', curso_views.cadastrar_curso, name='cadastrar_curso'),
    path('cursos/<int:curso_id>/editar/', curso_views.editar_curso, name='editar_curso'),
    path('login/', login_view, name='login'),
    path('register/', create_user_view, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])