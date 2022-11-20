from django.urls import path
from . import views as website_views

urlpatterns = [
    path('', website_views.Pagina_Inicial),
    path('send-message', website_views.Pagina_Inicial),
]