from django.urls import path
from . import views as website_views
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', RedirectView.as_view(url='dashboards/')),
    path('dashboards/', website_views.Painel_Administracao, name='dashboard'),
    path('emails/', website_views.Emails, name='emails'),
    path('login/', website_views.Login, name='login'),
    path('logout/', website_views.Logout, name='logout'),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)