from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('report/', views.report_crime, name='report_crime') ,
    path('view/',views.view_reports,name='view_reports'),
    path('statistics/', views.crime_statistics, name='crime_statistics'),
    path('about/', views.about, name='about'),


] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
